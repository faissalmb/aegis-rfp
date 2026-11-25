from enum import Enum
from typing import List
from pydantic import BaseModel, Field, field_validator


# 1. Enum : Limiter les valeurs possibles à une liste fermée
class ConfidenceLevel(str, Enum):
    HIGH = "high"       # Score >= 0.85 : Réponse fiable, prête à valider
    MEDIUM = "medium"   # Score 0.60 - 0.84 : Relecture humaine conseillée
    LOW = "low"         # Score < 0.60 : Info manquante ou risque d'hallucination


# 2. CitationSource : La preuve documentaire obligatoire (le cœur d'AegisRFP)
class CitationSource(BaseModel):
    document_name: str = Field(..., examples=["Etude_de_cas_Banque_2025.pdf"])
    page_number: int = Field(..., ge=1, description="Numéro de page strictement positif (>= 1)")
    excerpt: str = Field(..., min_length=10, description="Extrait exact tiré du document interne")


# 3. RFPQuestionRequest : Ce que l'utilisateur ou n8n envoie à notre API
class RFPQuestionRequest(BaseModel):
    rfp_id: str = Field(..., description="Identifiant unique de l'appel d'offres")
    question_text: str = Field(..., min_length=5, description="Exigence ou question du cahier des charges")
    client_industry: str = Field(default="B2B Services", description="Secteur d'activité du prospect")

    # Validateur personnalisé : nettoie automatiquement les espaces inutiles avant traitement
    @field_validator("question_text")
    @classmethod
    def clean_whitespace(cls, value: str) -> str:
        return " ".join(value.split())


# 4. RFPQuestionResponse : Ce que notre moteur IA garantit de renvoyer
class RFPQuestionResponse(BaseModel):
    rfp_id: str
    question_text: str
    generated_answer: str
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Score entre 0.0 et 1.0")
    confidence_level: ConfidenceLevel
    citations: List[CitationSource] = Field(default_factory=list)
    requires_human_review: bool


# 5. BatchRFPRequest : Permettre d'envoyer tout un appel d'offres (jusqu'à 50 questions d'un coup)
class BatchRFPRequest(BaseModel):
    rfp_id: str
    questions: List[RFPQuestionRequest] = Field(..., min_length=1, max_length=50)
