from fastapi import FastAPI
from routes.posiljke import router as posiljke_router

app = FastAPI(
    title="Shipping API",
    description="API za upravljanje pošiljkama",
    version="1.0.0"
)

app.include_router(posiljke_router)

@app.get("/")
async def root():
    """Root endpoint - dobrodošlica"""
    return {
        "message": "Dobrodošli u Shipping API",
        "verzija": "1.0.0"
    }
