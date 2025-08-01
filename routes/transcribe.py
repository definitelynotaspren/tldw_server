from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from utils.config import settings
from utils.logger import logger
from utils.sgf import generate_sgf
from utils.webhook import post_webhook

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post('/transcribe')
@limiter.limit(settings.RATE_LIMIT)
async def transcribe(request: Request, background_tasks: BackgroundTasks, audio: UploadFile = File(...), webhook_url: str | None = None):
    try:
        text = f"Transcribed {audio.filename}"
        logger.info(f"Transcribed file {audio.filename}")
        sgf_file = generate_sgf(text, '0', 'neutral', audio.filename)
        message = {"text": text, "sgf": str(sgf_file)}
        url = webhook_url or settings.WEBHOOK_URL
        if url:
            background_tasks.add_task(post_webhook, url, text)
        return JSONResponse(message)
    except Exception as e:
        logger.error(f"Transcription failed: {e}")
        raise HTTPException(status_code=500, detail={"error": "Transcription failed", "details": str(e)})
