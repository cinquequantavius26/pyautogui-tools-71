import pyautogui
import time
import random

def move_mouse(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)

def left_click(x=None, y=None, duration=0.5):
    if x is not None and y is not None:
        move_mouse(x, y, duration)
    pyautogui.click()

def right_click(x=None, y=None, duration=0.5):
    if x is not None and y is not None:
        move_mouse(x, y, duration)
    pyautogui.rightClick()

def double_click(x=None, y=None, duration=0.5):
    if x is not None and y is not None:
        move_mouse(x, y, duration)
    pyautogui.doubleClick()

def random_delay(min_seconds=0.1, max_seconds=0.5):
    time.sleep(random.uniform(min_seconds, max_seconds))

def get_position():
    return pyautogui.position()

def scroll(direction, amount=10):
    if direction.lower() == 'up':
        pyautogui.scroll(amount)
    else:
        pyautogui.scroll(-amount)

def press_hotkey(*keys):
    pyautogui.hotkey(*keys)

def type_string(text, interval=0.02):
    pyautogui.typewrite(text, interval=interval)

def drag_to(x, y, duration=1.0):
    pyautogui.dragTo(x, y, duration=duration)