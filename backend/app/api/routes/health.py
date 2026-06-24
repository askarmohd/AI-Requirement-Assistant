from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "success": True,
        "status": "healthy",
        "service": "AI Requirement Assistant",
        "version": "1.0.0"
    }