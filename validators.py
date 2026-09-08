from typing import Any, Union

def validate_coordinates(x: Any, y: Any) -> tuple[int, int]:
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError(f"Coordinates must be numeric, got {type(x)}, {type(y)}")
    return int(x), int(y)

def validate_interval(interval: Any) -> float:
    if not isinstance(interval, (int, float)) or interval < 0:
        raise ValueError(f"Interval must be non-negative number, got {interval}")
    return float(interval)

def validate_clicks(clicks: Any) -> int:
    if not isinstance(clicks, int) or clicks < 1:
        raise ValueError(f"Click count must be positive integer, got {clicks}")
    return clicks

def validate_button(button: str) -> str:
    valid = ('left', 'right', 'middle')
    if button not in valid:
        raise ValueError(f"Button must be one of {valid}, got {button}")
    return button