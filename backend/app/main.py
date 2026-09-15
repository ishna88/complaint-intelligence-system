"""
Complaint Intelligence System - FastAPI Backend
Phase 4: Minimal skeleton to verify environment setup.
Real /api/analyze logic will be added in Phase 7.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Complaint Intelligence System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "Complaint Intelligence backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}