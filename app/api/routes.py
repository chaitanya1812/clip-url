from fastapi import APIRouter
from .health import router as health_router

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to API"}

router.include_router(health_router)
