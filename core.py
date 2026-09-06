import time
import threading
import pyautogui

pyautogui.PAUSE = 0.001
pyautogui.FAILSAFE = True

class HighPerformanceClicker:
    def __init__(self, interval: float = 0.001, button: str = "left"):
        self.interval = interval
        self.button = button
        self._running = False
        self._thread = None

    def _click_loop(self):
        click_func = pyautogui.click
        button = self.button
        interval = self.interval
        
        while self._running:
            start_time = time.perf_counter()
            click_func(button=button)
            elapsed = time.perf_counter() - start_time
            sleep_time = interval - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)
            self._thread = None

    @property
    def is_running(self) -> bool:
        return self._running