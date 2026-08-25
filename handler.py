import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "pyautogui_tools.log"
    logger = logging.getLogger("pyautogui_tools")
    logger.setLevel(logging.DEBUG)
    if logger.handlers:
        return logger
    rotating_handler = RotatingFileHandler(
        log_file,
        maxBytes=10485760,
        backupCount=5
    )
    rotating_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger