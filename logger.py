import logging
import sys
from typing import Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance for the application.

    Args:
        name: The name of the logger.
        level: The logging threshold level.

    Returns:
        Configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Retrieves an existing logger or creates a new one.

    Args:
        name: The name of the logger to retrieve.

    Returns:
        The logger instance.
    """
    return logging.getLogger(name or "pyautogui-tools-71")