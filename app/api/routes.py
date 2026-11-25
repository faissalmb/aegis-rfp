import asyncio
from typing import List
from fastapi import APIRouter
from app.schemas.rfp import (
    BatchRFPRequest,
    CitationSource,
    ConfidenceLevel,
    RFPQuestionRequest,
    RFPQuestionResponse,
)

# 1. APIRouter : Permet de regrouper toutes les routes liées aux appels d'offres
router = APIRouter(prefix="/api/v1/rfp", tags=["RFP Engine"])


# 2. Fonction métier privée : Traduit le score numérique en feu tricolore
def _compute_confidence_level(score: float) -> ConfidenceLevel:
    if score >= 0.85:
        return ConfidenceLevel.HIGH
    if score >= 0.60:
        return ConfidenceLevel.MEDIUM
    return ConfidenceLevel.LOW


# 3. Cœur du traitement asynchrone pour UNE question
async def _process_single_question(req: RFPQuestionRequest) -> RFPQuestionResponse:
    # Simulation d'un temps d'attente réseau (appel Qdrant + LLM dans les prochaines phases)
    await asyncio.sleep(0.5)

    simulated_score = 0.91
    level = _compute_confidence_level(simulated_score)

    return RFPQuestionResponse(
        rfp_id=req.rfp_id,
        question_text=req.question_text,
        generated_answer=(
            f"Notre architecture garantit une isolation complète des données "
            f"pour le secteur {req.client_industry}."
        ),
        confidence_score=simulated_score,
        confidence_level=level,
        citations=[
            CitationSource(
                document_name="Architecture_Securite_B2B.pdf",
                page_number=12,
                excerpt="Toutes les données clients sont isolées par locataire et chiffrées au repos."
            )
        ],
        requires_human_review=(level != ConfidenceLevel.HIGH),
    )


# 4. Route POST pour traiter une seule question
@router.post("/answer", response_model=RFPQuestionResponse)
async def answer_single_question(request: RFPQuestionRequest) -> RFPQuestionResponse:
    return await _process_single_question(request)


# 5. Route POST pour traiter tout un lot de questions en parallèle
@router.post("/answer-batch", response_model=List[RFPQuestionResponse])
async def answer_batch_questions(batch: BatchRFPRequest) -> List[RFPQuestionResponse]:
    tasks = [_process_single_question(question) for question in batch.questions]
    return await asyncio.gather(*tasks)
