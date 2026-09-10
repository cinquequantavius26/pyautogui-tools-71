import pyautogui

def validate_coordinates(x: int, y: int) -> bool:
    screen_width, screen_height = pyautogui.size()
    return 0 <= x < screen_width and 0 <= y < screen_height

def validate_interval(interval: float) -> bool:
    return isinstance(interval, (int, float)) and interval >= 0

def validate_clicks(clicks: int) -> bool:
    return isinstance(clicks, int) and clicks > 0

def process_input(x: int, y: int, interval: float, clicks: int):
    if not validate_coordinates(x, y):
        raise ValueError(f"Invalid coordinates: ({x}, {y})")
    if not validate_interval(interval):
        raise ValueError(f"Invalid interval: {interval}")
    if not validate_clicks(clicks):
        raise ValueError(f"Invalid click count: {clicks}")

def execute_click(x: int, y: int, interval: float, clicks: int):
    process_input(x, y, interval, clicks)
    pyautogui.click(x=x, y=y, clicks=clicks, interval=interval)