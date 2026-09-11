import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = "autoclicker.log"
MAX_BYTES = 1 * 1024 * 1024
BACKUP_COUNT = 3

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        path = Path(LOG_FILE)
        handler = RotatingFileHandler(
            path,
            maxBytes=MAX_BYTES,
            backupCount=BACKUP_COUNT
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger