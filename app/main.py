from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from app.api.routes import router as api_router
from app.core.routes import router as core_router
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel
import os
from contextlib import asynccontextmanager
from app.core.db import *
from app.core.logic import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic here
    print("Starting up...")
    init_db()
    yield
    # Shutdown logic here
    print("Shutting down...")

app = FastAPI(title="ClipURL", lifespan=lifespan)

# @app.get("/")
# def root():
#     return {"message": "Welcome to ClipURL"}

# Serve /static/ folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def frontend():
    return FileResponse("app/static/index.html")

@app.get("/favicon.ico")
async def favicon():
    # app/media/favicon.ico
    file_path = os.path.join("app/media", "favicon.ico")
    return FileResponse(file_path, media_type="image/x-icon")

# include api router
app.include_router(api_router,  prefix="/api", tags=["api"])

# include core router
app.include_router(core_router,  prefix="/core", tags=["core"])



class URLRequest(BaseModel):
    original_url: str

@app.post("/shorten")
def shorten_url(data: URLRequest):
    print("shorten url req : ", data.original_url)
    result = create_shortened_url(data.original_url)
    return {"shortened_url": result["shortened_url"]}

@app.get("/go/{short_path}")
def redirect_to_original(short_path: str):
    from app.core.logic import _hash_short_path
    print("redirect_to_original : ", short_path)
    hash_value = _hash_short_path(short_path)
    original_url = resolve_shortened_url(hash_value)
    if original_url:
        return RedirectResponse(original_url)
    raise HTTPException(status_code=404, detail="Short URL not found")




@app.get("/get_all")
def get_all_urls():
    print("get all urls : ")
    data = get_all_url_entries()
    if data!=None:
        return{"data":data}
    raise HTTPException(status_code=500, detail="something went wrong")