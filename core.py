import pyautogui
import time
from typing import Tuple

class AutoClicker:
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._running = False
        pyautogui.PAUSE = 0

    def start(self, duration: int = None):
        self._running = True
        start_time = time.perf_counter()
        
        try:
            while self._running:
                pyautogui.click(_pause=False)
                time.sleep(self.interval)
                
                if duration and (time.perf_counter() - start_time) > duration:
                    break
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self._running = False

    def set_position(self, x: int, y: int):
        pyautogui.moveTo(x, y, _pause=False)

    @staticmethod
    def get_position() -> Tuple[int, int]:
        return pyautogui.position()