import re


def validate_coordinate(value: int) -> int:
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"Invalid coordinate: {value}. Must be non-negative integer.")
    return value


def validate_interval(value: float) -> float:
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"Invalid interval: {value}. Must be positive number.")
    return float(value)


def validate_hotkey(key: str) -> str:
    if not re.match(r'^[a-zA-Z0-9+]+$', key):
        raise ValueError(f"Invalid hotkey format: {key}.")
    return key


def validate_clicks(count: int) -> int:
    if not isinstance(count, int) or count < -1:
        raise ValueError(f"Invalid click count: {count}. Must be -1 or positive.")
    return count