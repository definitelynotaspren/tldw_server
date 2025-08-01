from utils.summarize import simple_summarize
from utils.sgf import generate_sgf
from pathlib import Path


def test_simple_summarize():
    text = "word " * 100
    summary = simple_summarize(text, max_words=5)
    assert summary.startswith("word word word word word")


def test_generate_sgf(tmp_path):
    sgf = generate_sgf("hello", "1", "happy", "hi")
    assert Path(sgf).exists()
    Path(sgf).unlink()
