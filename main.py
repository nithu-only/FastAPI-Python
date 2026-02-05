#import the module
import uvicorn
from app.api import app


if __name__ == "__main__":
    # creating lightning-fast ASGI web server implementation
    # ASGI (Asynchronous Server Gateway Interface)
    uvicorn.run(
        # Your app() in this case {inside app folder -> api.py -> app function}
        "app.api:app",
        port=8000,
        host="0.0.0.0",
        reload=True 
    )

