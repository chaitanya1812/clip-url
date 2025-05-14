from fastapi import FastAPI
from app.routes import router as url_router
# from app.db import init_db

app = FastAPI(title="URL Service")

# @app.on_event("startup")
# async def startup_event():
#     init_db()

app.include_router(url_router)
