import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = "autoclicker.log"
MAX_BYTES = 1024 * 1024
BACKUP_COUNT = 3

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backup_count=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger