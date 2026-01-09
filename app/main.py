from fastapi import FastAPI
from api.router import api_router

app: FastAPI = FastAPI(
    title="Auth API", 
    description="This a API for authentication user",
    version="1.0.0"
)

app.include_router(api_router)