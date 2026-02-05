"""
    Importing APIRouter class from fast API to create routes to the API
    #Importing HTTPException to catch if any exception occure during the API call
"""
from fastapi import APIRouter,HTTPException
#Importing service logic from our metric_service function
from services.metrics_service import get_system_metrics
# Creating router object of APIRouter class to create route to the API call
router = APIRouter()

@router.get("/metrics")
def get_metrics():
    # Handling Exception which may cause in API call
    try:
        metrics = get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )