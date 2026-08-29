import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "autoclicker.log"
MAX_LOG_SIZE = 5 * 1024 * 1024
BACKUP_COUNT = 3

def setup_logger(level=logging.INFO):
    LOG_DIR.mkdir(exist_ok=True)
    logger = logging.getLogger("autoclicker")
    logger.setLevel(level)
    if any(isinstance(h, RotatingFileHandler) for h in logger.handlers):
        return logger
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    return logger