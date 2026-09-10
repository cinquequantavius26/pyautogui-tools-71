import time
import threading
import pyautogui

pyautogui.PAUSE = 0.0001
pyautogui.FAILSAFE = True

class RapidClicker:
    def __init__(self, interval=0.001, button='left'):
        self.interval = interval
        self.button = button
        self.is_running = False
        self._thread = None

    def _click_loop(self):
        click_func = pyautogui.click
        sleep_func = time.sleep
        interval = self.interval
        button = self.button
        
        while self.is_running:
            click_func(button=button)
            if interval > 0:
                sleep_func(interval)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self):
        self.is_running = False
        if self._thread:
            self._thread.join(timeout=0.5)