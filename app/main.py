from fastapi import FastAPI
from app.routes.mediciones import router as measurements_router

app = FastAPI(title="Backend Proyecto Quinua")

app.include_router(
    measurements_router,
    prefix="/api/v1",
    tags=["Measurements"],
)
