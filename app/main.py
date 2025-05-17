from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.routes import router as core_router

app = FastAPI(title="ClipURL")

@app.get("/")
def root():
    return {"message": "Welcome to ClipURL"}

# include api router
app.include_router(api_router,  prefix="/api", tags=["api"])

# include core router
app.include_router(core_router,  prefix="/core", tags=["core"])
