import time
import random
from typing import Tuple


def calculate_jitter(base_interval: float, jitter_range: float) -> float:
    """Calculate click interval with randomized jitter."""
    jitter = random.uniform(-jitter_range, jitter_range)
    return max(0.01, base_interval + jitter)


def sleep_with_jitter(base_interval: float, jitter_range: float) -> None:
    """Sleep for a duration adjusted by jitter."""
    actual_interval = calculate_jitter(base_interval, jitter_range)
    time.sleep(actual_interval)


def validate_coordinates(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    """Validate if coordinates are within screen boundaries."""
    width, height = screen_size
    return 0 <= x < width and 0 <= y < height


def format_elapsed_time(seconds: float) -> str:
    """Format elapsed seconds into a readable string."""
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"
