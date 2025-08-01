from datetime import datetime
from pathlib import Path
from .config import settings


def generate_sgf(text: str, breath_marker: str, emotional_trace: str, symbolic_anchor: str) -> Path:
    timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%S')
    filename = settings.SGF_OUTPUT_DIR / f"{timestamp}.sgf"
    content = {
        "breath_marker": breath_marker,
        "emotional_trace": emotional_trace,
        "symbolic_anchor": symbolic_anchor,
        "text": text,
    }
    with open(filename, 'w', encoding='utf-8') as f:
        for k, v in content.items():
            f.write(f"{k}: {v}\n")
    return filename
