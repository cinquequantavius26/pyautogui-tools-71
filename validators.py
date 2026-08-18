import re

def validate_click_rate(click_rate):
    if not isinstance(click_rate, (int, float)):
        raise ValueError('Click rate must be a number.')
    if click_rate <= 0:
        raise ValueError('Click rate must be greater than zero.')


def validate_duration(duration):
    if not isinstance(duration, (int, float)):
        raise ValueError('Duration must be a number.')
    if duration <= 0:
        raise ValueError('Duration must be greater than zero.')


def validate_coordinates(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError('Coordinates must be integers.')
    if x < 0 or y < 0:
        raise ValueError('Coordinates must be non-negative integers.')


def validate_inputs(click_rate, duration, x, y):
    validate_click_rate(click_rate)
    validate_duration(duration)
    validate_coordinates(x, y)