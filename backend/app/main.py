from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.devices import router as devices_router

app = FastAPI(
    title="GamePerf Analyzer API",
    description="Android game performance analysis platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

app.include_router(devices_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}