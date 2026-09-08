import pyautogui
import time
from typing import Tuple

def get_mouse_position() -> Tuple[int, int]:
    return pyautogui.position()

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    pyautogui.click(x, y)
    time.sleep(interval)

def validate_coordinates(x: int, y: int) -> bool:
    screen_width, screen_height = pyautogui.size()
    return 0 <= x <= screen_width and 0 <= y <= screen_height

def perform_sequence(coords: list[Tuple[int, int]], delay: float = 0.5) -> None:
    for x, y in coords:
        if validate_coordinates(x, y):
            safe_click(x, y, delay)

def emergency_stop(key: str = 'esc') -> None:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1