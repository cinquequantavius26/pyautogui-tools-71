import time
import pyautogui


class MouseClickHandler:
    def __init__(self, default_delay: float = 0.1) -> None:
        self.default_delay = default_delay
        pyautogui.FAILSAFE = True

    def click_at(self, x: int, y: int, clicks: int = 1, interval: float = 0.0) -> None:
        pyautogui.click(x=x, y=y, clicks=clicks, interval=interval)

    def double_click_at(self, x: int, y: int) -> None:
        pyautogui.doubleClick(x=x, y=y)

    def move_and_click(self, x: int, y: int, duration: float = 0.2) -> None:
        pyautogui.moveTo(x, y, duration=duration)
        pyautogui.click()

    def click_sequence(self, points: list[tuple[int, int]], interval: float = 0.5) -> None:
        for x, y in points:
            pyautogui.click(x, y)
            time.sleep(interval)
