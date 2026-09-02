import time
from functools import wraps

class NetworkError(Exception):
    pass

class ConnectionError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class MaxRetriesExceeded(NetworkError):
    pass

def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as exc:
                    last_exc = exc
                    if i < max_retries - 1:
                        time.sleep(delay)
            if last_exc:
                raise MaxRetriesExceeded("Maximum retries exceeded") from last_exc
            raise MaxRetriesExceeded("Maximum retries exceeded")
        return wrapper
    return decorator

class RetryManager:
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay
    def run(self, operation):
        last_exc = None
        for attempt in range(self.max_retries):
            try:
                return operation()
            except (ConnectionError, TimeoutError) as exc:
                last_exc = exc
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay)
        raise MaxRetriesExceeded("Max retries exceeded") from last_exc