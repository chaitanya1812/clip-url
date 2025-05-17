from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.routes import router as core_router
from fastapi.responses import FileResponse
import os

app = FastAPI(title="ClipURL")

@app.get("/")
def root():
    return {"message": "Welcome to ClipURL"}

@app.get("/favicon.ico")
async def favicon():
    # app/media/favicon.ico
    file_path = os.path.join("app/media", "favicon.ico")
    return FileResponse(file_path, media_type="image/x-icon")

# include api router
app.include_router(api_router,  prefix="/api", tags=["api"])

# include core router
app.include_router(core_router,  prefix="/core", tags=["core"])
