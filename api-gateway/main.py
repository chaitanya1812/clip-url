from fastapi import FastAPI
from app.health import router as health_router

app = FastAPI(title="API Gateway")
app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "Welcome to ClipURL API Gateway"}
