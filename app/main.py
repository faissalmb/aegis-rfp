from fastapi import FastAPI
from app.api.routes import router as rfp_router

app = FastAPI(
    title="AegisRFP API",
    description="Reliable B2B RAG & AI Agent Engine for Automated RFP Analysis",
    version="0.1.0",
)

# Branchement du routeur RFP sur l'application principale
app.include_router(rfp_router)


# Endpoint de santé (Health Check) indispensable en production
@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "service": "AegisRFP", "version": "0.1.0"}
