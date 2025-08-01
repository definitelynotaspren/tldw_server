from fastapi import APIRouter, HTTPException, BackgroundTasks, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from utils.config import settings
from utils.logger import logger
from utils.sgf import generate_sgf
from utils.webhook import post_webhook
from utils.summarize import simple_summarize

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

class SummaryRequest(BaseModel):
    text: str

@router.post('/summarize')
@limiter.limit(settings.RATE_LIMIT)
async def summarize(request: Request, body: SummaryRequest, background_tasks: BackgroundTasks, webhook_url: str | None = None):
    try:
        summary = simple_summarize(body.text)
        sgf_file = generate_sgf(summary, '0', 'neutral', summary[:10])
        logger.info("Summary generated")
        url = webhook_url or settings.WEBHOOK_URL
        if url:
            background_tasks.add_task(post_webhook, url, summary)
        return JSONResponse({"summary": summary, "sgf": str(sgf_file)})
    except Exception as e:
        logger.error(f"Summarization failed: {e}")
        raise HTTPException(status_code=500, detail={"error": "Summarization failed", "details": str(e)})
