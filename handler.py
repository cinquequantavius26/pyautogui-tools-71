import time
from typing import Tuple, Optional
import pyautogui

class ClickHandler:
    """Handles PyAutoGUI mouse interactions including clicking and dragging."""

    def __init__(self, interval: float = 0.1, clicks: int = 1) -> None:
        self.interval: float = interval
        self.clicks: int = clicks
        pyautogui.FAILSAFE = True

    def click_at(self, x: int, y: int, button: str = "left") -> bool:
        """Executes a mouse click at the specified coordinates."""
        try:
            pyautogui.click(x=x, y=y, clicks=self.clicks, interval=self.interval, button=button)
            return True
        except pyautogui.FailSafeException:
            return False

    def get_mouse_position(self) -> Tuple[int, int]:
        """Retrieves the current coordinates of the mouse cursor."""
        x, y = pyautogui.position()
        return int(x), int(y)

    def drag_to(self, x: int, y: int, duration: float = 0.5) -> bool:
        """Drags the mouse to target coordinates over specified duration."""
        try:
            pyautogui.dragTo(x, y, duration=duration)
            return True
        except pyautogui.FailSafeException:
            return False