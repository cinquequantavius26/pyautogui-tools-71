import time
import functools
from typing import Any, Callable, Optional

class NetworkRetry:
    def __init__(self, max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Optional[Exception] = None
            current_delay = self.delay
            for attempt in range(self.max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, OSError) as error:
                    last_error = error
                    if attempt < self.max_retries - 1:
                        time.sleep(current_delay)
                        current_delay *= self.backoff
            if last_error is not None:
                raise last_error
        return wrapper

def retry_network_operation(max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0) -> Callable:
    return NetworkRetry(max_retries, delay, backoff)