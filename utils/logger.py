import logging
from pythonjsonlogger import jsonlogger
from .config import settings

LEVEL = logging.DEBUG if settings.DEBUG else getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

logger = logging.getLogger("tldw")
logger.setLevel(LEVEL)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
