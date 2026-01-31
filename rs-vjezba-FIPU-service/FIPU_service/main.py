from fastapi import FastAPI
from routes.studenti import router as studenti_router
from routes.kolegiji import router as kolegiji_router

app = FastAPI()

app.include_router(studenti_router)
app.include_router(kolegiji_router)

@app.get("/")
async def root():
    return {"message": "FIPU Service is running"}

