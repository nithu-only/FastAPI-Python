from fastapi import FastAPI
from routers import metrics

#creating object of FastAPI to create a api
app = FastAPI(
    title="Internal Devops Utilities API",
    description="This is the Simple API Created using FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

#creating Route /
@app.get("/")
def hello():
    """
    Test API for Testing
    """
    return {
        "name":"Nithinkumar M",
        "role":"Devops guy"
            }

app.include_router(metrics.router)


