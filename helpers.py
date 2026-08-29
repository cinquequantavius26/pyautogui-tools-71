import pyautogui
import time
import random
from typing import Tuple

def move_and_click(x: int, y: int, clicks: int = 1, interval: float = 0.0, button: str = "left", delay: float = 0.05) -> None:
    """Move mouse to position and click.

    Args:
        x: X coordinate on screen.
        y: Y coordinate on screen.
        clicks: Number of clicks to perform.
        interval: Seconds between multiple clicks.
        button: Mouse button ('left', 'right', 'middle').
        delay: Additional delay after clicking.
    """
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks, interval=interval, button=button)
    time.sleep(delay)

def click_in_region(region: Tuple[int, int, int, int], num_clicks: int = 10, min_delay: float = 0.1, max_delay: float = 0.5) -> None:
    """Perform multiple random clicks inside a region.

    Args:
        region: (left, top, width, height).
        num_clicks: Total clicks to execute.
        min_delay: Minimum seconds between clicks.
        max_delay: Maximum seconds between clicks.
    """
    left, top, width, height = region
    for _ in range(num_clicks):
        click_x = left + random.randint(0, width)
        click_y = top + random.randint(0, height)
        pyautogui.click(click_x, click_y)
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

def get_current_position() -> Tuple[int, int]:
    """Get the current mouse cursor position.

    Returns:
        Tuple of (x, y) coordinates.
    """
    return pyautogui.position()

def press_keys(key: str, count: int = 1, interval: float = 0.05) -> None:
    """Press a key a number of times.

    Args:
        key: The key name to press.
        count: How many times to press it.
        interval: Time between presses.
    """
    pyautogui.press(key, presses=count, interval=interval)

def type_string(text: str, interval: float = 0.02) -> None:
    """Type out a string of characters.

    Args:
        text: The text to type.
        interval: Delay between each character.
    """
    pyautogui.typewrite(text, interval=interval)

def scroll(amount: int, delay: float = 0.1) -> None:
    """Scroll vertically by the given amount.

    Args:
        amount: Pixels or units to scroll. Positive scrolls up.
        delay: Pause after scrolling.
    """
    pyautogui.scroll(amount)
    time.sleep(delay)
