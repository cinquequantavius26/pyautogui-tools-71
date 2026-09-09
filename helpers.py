import pyautogui
import time
import random
from typing import Tuple

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    pyautogui.click(x, y)
    time.sleep(interval)

def random_jitter(x: int, y: int, radius: int = 5) -> Tuple[int, int]:
    offset_x = random.randint(-radius, radius)
    offset_y = random.randint(-radius, radius)
    return x + offset_x, y + offset_y

def perform_human_click(x: int, y: int) -> None:
    jx, jy = random_jitter(x, y)
    pyautogui.moveTo(jx, jy, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

def drag_to_location(start: Tuple[int, int], end: Tuple[int, int]) -> None:
    pyautogui.moveTo(*start)
    pyautogui.dragTo(*end, duration=random.uniform(0.5, 1.2))

def check_screen_bounds(x: int, y: int) -> bool:
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height