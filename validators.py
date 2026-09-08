from typing import Tuple, Union


def validate_coordinates(coords: Union[Tuple[int, int], None]) -> bool:
    """Validate that coordinates are either None or a pair of non-negative integers."""
    if coords is None:
        return True
    if not isinstance(coords, tuple) or len(coords) != 2:
        return False
    return (
        isinstance(coords[0], int)
        and isinstance(coords[1], int)
        and coords[0] >= 0
        and coords[1] >= 0
    )


def validate_interval(interval: float) -> bool:
    """Validate that the click interval is a non-negative number."""
    return isinstance(interval, (int, float)) and interval >= 0.0


def validate_button(button: str) -> bool:
    """Validate that the mouse button is one of the allowed options."""
    return button in {"left", "right", "middle"}


def validate_click_count(count: int) -> bool:
    """Validate that the click count is a non-negative integer."""
    return isinstance(count, int) and count >= 0
