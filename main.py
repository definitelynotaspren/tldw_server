from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.middleware.cors import CORSMiddleware

from utils.config import settings
from utils.logger import logger
from routes.transcribe import router as transcribe_router
from routes.summarize import router as summarize_router

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="tldw server", version="0.2.0")
app.state.limiter = limiter

app.add_middleware(CORSMiddleware, allow_origins=["*"])  # simple CORS

app.include_router(transcribe_router)
app.include_router(summarize_router)

@app.get("/")
async def root():
    return {"message": "tldw server"}
