from fastapi import FastAPI
from routes.posiljke import router as posiljke_router

app = FastAPI()

app.include_router(posiljke_router)

# cd shipping/shippingAPI
# pip install -r requirements.txt
# conda activate shippingAPI
# fastapi dev main.py