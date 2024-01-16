from fastapi import FastAPI
from src.routes.gpt_router import router

# Server running
app = FastAPI();

# Router
app.include_router(router);