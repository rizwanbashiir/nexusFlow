
from fastapi import FastAPI

app = FastAPI(
    title="NexusFlow Identity Service",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "identity-service",
    }
