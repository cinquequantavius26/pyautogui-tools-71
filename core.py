import time
from functools import wraps

def optimize_clicks(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration < 0.01:
            time.sleep(max(0.0, 0.01 - duration))
        return result
    return wrapper

class FastClicker:
    def __init__(self, interval: float = 0.01):
        self.interval = max(0.001, interval)
        self._last_click = 0.0

    @optimize_clicks
    def click(self, x: int, y: int) -> tuple[int, int]:
        now = time.perf_counter()
        elapsed = now - self._last_click
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self._last_click = time.perf_counter()
        return (x, y)

    def batch_click(self, coordinates: list[tuple[int, int]]) -> int:
        executed = 0
        for x, y in coordinates:
            self.click(x, y)
            executed += 1
        return executed
