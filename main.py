from fastapi import FastAPI
from app.routers import transform

app = FastAPI(title="Job Transformer API")

app.include_router(transform.router)
