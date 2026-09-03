import pyautogui
import time
from typing import Tuple

def validate_coordinates(x: int, y: int) -> bool:
    screen_width, screen_height = pyautogui.size()
    return 0 <= x < screen_width and 0 <= y < screen_height

def validate_interval(interval: float) -> bool:
    return isinstance(interval, (int, float)) and interval >= 0

def run_click_loop(x: int, y: int, interval: float, count: int) -> None:
    if not validate_coordinates(x, y):
        raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
    
    if not validate_interval(interval):
        raise ValueError(f"Invalid interval: {interval}")

    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")

    for _ in range(count):
        pyautogui.click(x, y)
        time.sleep(interval)

if __name__ == "__main__":
    try:
        run_click_loop(100, 100, 0.5, 10)
    except (ValueError, pyautogui.PyAutoGUIException) as e:
        print(f"Processing error: {e}")