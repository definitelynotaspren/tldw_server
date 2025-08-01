import json
import requests
from .logger import logger


def post_webhook(url: str, message: str) -> bool:
    try:
        response = requests.post(url, json={"content": message}, timeout=10)
        logger.debug(f"Webhook response: {response.status_code}")
        return response.status_code < 300
    except Exception as e:
        logger.error(f"Webhook failed: {e}")
        return False
