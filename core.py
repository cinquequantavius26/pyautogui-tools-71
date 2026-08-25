import pyautogui
import time
import threading

class ClickCore:
    def __init__(self):
        self.interval = 0.05
        self.active = False
        self.thread = None
        self.lock = threading.Lock()

    def set_interval(self, interval):
        with self.lock:
            self.interval = max(0.001, interval)

    def start_continuous(self):
        with self.lock:
            if self.active:
                return
            self.active = True
            self.thread = threading.Thread(target=self._run_loop, daemon=True)
            self.thread.start()

    def stop(self):
        with self.lock:
            self.active = False
        if self.thread is not None:
            self.thread.join(timeout=1)
            self.thread = None

    def _run_loop(self):
        next_time = time.perf_counter()
        while True:
            with self.lock:
                if not self.active:
                    break
                current_interval = self.interval
            pyautogui.click()
            next_time += current_interval
            sleep_duration = next_time - time.perf_counter()
            if sleep_duration > 0:
                time.sleep(sleep_duration)
            else:
                next_time = time.perf_counter()

    def click_fixed(self, count):
        if count <= 0:
            return
        next_time = time.perf_counter()
        for _ in range(count):
            pyautogui.click()
            next_time += self.interval
            sleep_duration = next_time - time.perf_counter()
            if sleep_duration > 0:
                time.sleep(sleep_duration)
            else:
                next_time = time.perf_counter()