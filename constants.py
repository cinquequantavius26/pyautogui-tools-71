from enum import Enum, unique

@unique
class MouseButton(str, Enum):
    LEFT = "left"
    MIDDLE = "middle"
    RIGHT = "right"

@unique
class ClickType(str, Enum):
    SINGLE = "single"
    DOUBLE = "double"
    TRIPLE = "triple"

DEFAULT_INTERVAL = 0.1
DEFAULT_DURATION = 0.0
MIN_CLICK_DELAY = 0.001
MAX_CLICK_DELAY = 3600.0

DEFAULT_HOTKEY_START_STOP = "f8"
DEFAULT_HOTKEY_EXIT = "f12"
