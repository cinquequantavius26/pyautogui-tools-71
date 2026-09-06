import random
import time
from typing import Tuple, Optional


def random_sleep(min_seconds: float, max_seconds: float) -> None:
    if min_seconds < 0 or max_seconds < min_seconds:
        raise ValueError("Invalid sleep duration parameters")
    duration = random.uniform(min_seconds, max_seconds)
    time.sleep(duration)


def calculate_interval(clicks_per_second: float) -> float:
    if clicks_per_second <= 0:
        raise ValueError("Clicks per second must be greater than zero")
    return 1.0 / clicks_per_second


def is_within_bounds(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    width, height = screen_size
    return 0 <= x < width and 0 <= y < height


def parse_coordinates(coord_str: str) -> Optional[Tuple[int, int]]:
    try:
        parts = coord_str.strip().split(",")
        if len(parts) != 2:
            return None
        return int(parts[0].strip()), int(parts[1].strip())
    except ValueError:
        return None
