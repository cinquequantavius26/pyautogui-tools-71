class AutoClickerError(Exception):
    """Base exception for the toolkit."""

class CoordinateOutOfBoundsError(AutoClickerError):
    """Raised when coordinates fall outside screen resolution."""

class ConfigurationError(AutoClickerError):
    """Raised when input parameters are invalid."""

class ExecutionError(AutoClickerError):
    """Raised during click sequence failures."""

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> None:
    if not (0 <= x < screen_width and 0 <= y < screen_height):
        raise CoordinateOutOfBoundsError(f"({x}, {y}) outside resolution {screen_width}x{screen_height}")

def validate_interval(interval: float) -> None:
    if interval < 0:
        raise ConfigurationError(f"Invalid interval: {interval}. Must be non-negative.")
