import pyautogui
def validate_positive_integer(value, name='value'):
    if not isinstance(value, int):
        raise ValueError(f'{name} must be an integer')
    if value <= 0:
        raise ValueError(f'{name} must be greater than zero')
    return value

def validate_positive_float(value, name='value'):
    if not isinstance(value, (int, float)):
        raise ValueError(f'{name} must be a number')
    if value <= 0:
        raise ValueError(f'{name} must be greater than zero')
    return float(value)

def validate_screen_coordinates(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('X and Y must be integers')
    try:
        screen_width, screen_height = pyautogui.size()
    except Exception:
        raise RuntimeError('Unable to determine screen dimensions')
    if x < 0 or x >= screen_width:
        raise ValueError(f'X {x} outside screen range 0 to {screen_width - 1}')
    if y < 0 or y >= screen_height:
        raise ValueError(f'Y {y} outside screen range 0 to {screen_height - 1}')
    return x, y

def validate_mouse_button(button):
    allowed = ['left', 'right', 'middle']
    if button not in allowed:
        raise ValueError(f'Invalid button \'{button}\', use {allowed}')
    return button

def validate_autoclick_params(clicks, delay, button='left', position=None):
    clicks = validate_positive_integer(clicks, 'clicks')
    delay = validate_positive_float(delay, 'delay')
    if clicks > 10000:
        raise ValueError('Maximum clicks is 10000 to prevent abuse')
    if delay < 0.001:
        raise ValueError('Minimum delay is 0.001 seconds')
    button = validate_mouse_button(button)
    if position is not None:
        if not isinstance(position, (list, tuple)) or len(position) != 2:
            raise ValueError('Position must be a tuple or list of two integers')
        x, y = position
        validate_screen_coordinates(x, y)
    return clicks, delay, button, position