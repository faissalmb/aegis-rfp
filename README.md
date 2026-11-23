# AegisRFP 🛡️

**Reliable B2B RAG & AI Agent Engine for Automated RFP (Request for Proposal) Analysis and Sales Intelligence.**

## 🎯 Overview
AegisRFP is a production-oriented AI engineering system designed to help B2B service agencies and consulting firms automate tender responses and outbound prospecting without hallucinations. It connects internal company knowledge bases (PDFs, past proposals, case studies) to an evaluated hybrid RAG pipeline and automated workflows.

## 🏗️ Project Architecture

```text
aegis-rfp/
├── app/
│   ├── api/            # Async FastAPI endpoints
│   ├── schemas/        # Strict Pydantic data contracts
│   ├── core/           # Configuration, environment settings & security
│   ├── services/       # Document parsing, embeddings & Qdrant hybrid search
│   ├── agents/         # Tool calling & LangGraph orchestration workflows
│   └── evaluation/     # RAGAS / DeepEval anti-hallucination pipelines
├── tests/              # Automated unit & integration tests
├── .gitignore          # Ignored local & sensitive files
└── README.md           # Project documentation
```

## 🚀 Roadmap & Build Progress
- [x] **Phase 1 (In Progress):** Modular architecture, strict Pydantic schemas & async FastAPI core
- [ ] **Phase 2:** LLM Structured Outputs & Tool Calling for RFP requirement extraction
- [ ] **Phase 3:** Hybrid RAG Engine (Qdrant + BM25 + Reranking)
- [ ] **Phase 4:** Multi-step LangGraph Agents & n8n B2B outreach connectors
- [ ] **Phase 5:** Automated evaluation pipeline (RAGAS Faithfulness & Context Recall)
- [ ] **Phase 6:** Human-in-the-loop UI & Docker Compose deployment
