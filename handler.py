import pyautogui
import logging
from typing import Tuple, Optional

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def safe_click(x: int, y: int, button: str = 'left') -> bool:
    try:
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
        
        pyautogui.click(x=x, y=y, button=button)
        return True
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered by user")
        return False
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected automation error: {e}")
        return False

def get_safe_position() -> Optional[Tuple[int, int]]:
    try:
        pos = pyautogui.position()
        return (pos.x, pos.y)
    except pyautogui.FailSafeException:
        return None
    except Exception as e:
        logger.error(f"Position retrieval failure: {e}")
        return None