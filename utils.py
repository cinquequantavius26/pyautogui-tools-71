import time
import functools
import requests
from typing import Callable, Any

def retry_network_op(retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=2.0)
def fetch_remote_config(url: str) -> dict:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()