class ValidationError(Exception):
    pass

def validate_coordinates(x: int, y: int) -> None:
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError("Coordinates must be integers")
    if x < 0 or y < 0:
        raise ValidationError("Coordinates must be non-negative")

def validate_interval(interval: float) -> None:
    if not isinstance(interval, (int, float)):
        raise ValidationError("Interval must be numeric")
    if interval < 0.001:
        raise ValidationError("Interval too low, minimum is 0.001")

def validate_clicks(clicks: int) -> None:
    if not isinstance(clicks, int) or clicks < 1:
        raise ValidationError("Click count must be a positive integer")
