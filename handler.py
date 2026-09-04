import time
from functools import wraps
from typing import Any, Callable, Type, Tuple

def with_retry(
    retries: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError)
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
            if last_exception:
                raise last_exception
            raise RuntimeError("Operation failed after maximum retries")
        return wrapper
    return decorator
