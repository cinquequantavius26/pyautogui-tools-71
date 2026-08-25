import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_name: str = "pyautogui_tools") -> logging.Logger:
    logger = logging.getLogger(log_name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"{log_name}.log")
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1024 * 1024 * 5, backupCount=5
        )
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(file_handler)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(stream_handler)
    return logger