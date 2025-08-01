from .logger import logger


def simple_summarize(text: str, max_words: int = 50) -> str:
    words = text.split()
    summary = ' '.join(words[:max_words])
    if len(words) > max_words:
        summary += '...'
    logger.debug(f"Summary: {summary}")
    return summary
