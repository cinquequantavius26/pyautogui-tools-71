import time
from functools import wraps
import socket
import urllib.request
import urllib.error

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    exceptions = (urllib.error.URLError, urllib.error.HTTPError, socket.timeout, ConnectionError, TimeoutError)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def safe_network_call(func, *args, **kwargs):
    decorated = retry_network_operation(max_retries=4, delay=0.5)(func)
    return decorated(*args, **kwargs)

def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL')
    return url

def get_with_retry(url):
    validate_url(url)
    @retry_network_operation(max_retries=3)
    def inner():
        with urllib.request.urlopen(url) as resp:
            return resp.read()
    return inner()