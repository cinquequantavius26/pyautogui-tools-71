from typing import Tuple


def click_position(x: int, y: int) -> None:
    """
    Simulates a mouse click at the given (x, y) coordinates.

    :param x: The x-coordinate where the click should occur.
    :param y: The y-coordinate where the click should occur.
    """
    import pyautogui
    pyautogui.click(x, y)


def get_mouse_position() -> Tuple[int, int]:
    """
    Retrieves the current position of the mouse cursor.

    :return: A tuple containing the current (x, y) coordinates of the mouse cursor.
    """
    import pyautogui
    return pyautogui.position()


def wait_for_click() -> None:
    """
    Waits for a mouse click to occur.
    """
    import pyautogui
    pyautogui.wait('click')


def click_multiple_times(x: int, y: int, times: int) -> None:
    """
    Clicks at the specified position a defined number of times.

    :param x: The x-coordinate where the clicks should occur.
    :param y: The y-coordinate where the clicks should occur.
    :param times: The number of times to click.
    """
    for _ in range(times):
        click_position(x, y)  
        
