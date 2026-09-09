from typing import Optional, Tuple


class ValidationError(ValueError):
    """Raised when autoclicker configuration parameters are invalid."""
    pass


def validate_interval(interval: float) -> float:
    if not isinstance(interval, (int, float)):
        raise ValidationError("Interval must be a numeric value.")
    if interval < 0.001:
        raise ValidationError("Interval must be at least 0.001 seconds.")
    return float(interval)


def validate_clicks(clicks: int) -> int:
    if not isinstance(clicks, int):
        raise ValidationError("Clicks count must be an integer.")
    if clicks < 0:
        raise ValidationError("Clicks count cannot be negative (use 0 for infinite).")
    return clicks


def validate_button(button: str) -> str:
    valid_buttons = {"left", "right", "middle", "primary", "secondary"}
    if not isinstance(button, str):
        raise ValidationError("Button must be a string.")
    cleaned_button = button.lower().strip()
    if cleaned_button not in valid_buttons:
        raise ValidationError(f"Invalid button '{button}'. Must be one of {valid_buttons}.")
    return cleaned_button


def validate_coordinates(coords: Optional[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
    if coords is None:
        return None
    if not isinstance(coords, tuple) or len(coords) != 2:
        raise ValidationError("Coordinates must be a tuple of (x, y) or None.")
    x, y = coords
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError("Coordinates must contain only integers.")
    if x < 0 or y < 0:
        raise ValidationError("Coordinates cannot be negative values.")
    return x, y
