import time
import random
from functools import wraps
from typing import Callable, Any, Tuple, Type
import urllib.request
import urllib.error

def retry_network(
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (urllib.error.URLError, ConnectionError)
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries - 1:
                        raise e
                    sleep_time = current_delay + random.uniform(0, 0.5)
                    time.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator

def fetch_url(url: str, timeout: float = 5.0) -> bytes:
    @retry_network()
    def _fetch() -> bytes:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read()
    return _fetch()