import pyautogui
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

def safe_click(x: int, y: int) -> bool:
    try:
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.error(f"Coordinates ({x}, {y}) out of bounds")
            return False
        
        pyautogui.click(x, y)
        return True
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered by user")
        return False
    except Exception as e:
        logger.error(f"Unexpected automation failure: {e}")
        return False

def get_valid_position(x: str, y: str) -> Optional[Tuple[int, int]]:
    try:
        pos_x, pos_y = int(x), int(y)
        return (pos_x, pos_y)
    except (ValueError, TypeError) as e:
        logger.warning(f"Invalid coordinate input: {e}")
        return None

def perform_click_sequence(coords: list) -> int:
    successful_clicks = 0
    for x, y in coords:
        if safe_click(x, y):
            successful_clicks += 1
        else:
            break
    return successful_clicks