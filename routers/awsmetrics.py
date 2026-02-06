"""
    Importing APIRouter class from fast API to create routes to the API
    #Importing HTTPException to catch if any exception occure during the API call
"""
from fastapi import APIRouter,HTTPException
#Importing service logic from our metric_service function
from services.s3_service import get_s3_buckets
# Creating router object of APIRouter class to create route to the API call
router = APIRouter()

@router.get("/s3", status_code=200)
def get_buckets():
    # Handling Exception which may cause in API call
    try:
        buckets = get_s3_buckets()
        return buckets
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    
@router.get("/ec2",status_code=200)
def get_instance():
    return {"status":"Amazon ec2 creation is in progress"}