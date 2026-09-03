# pyautogui-tools-71

A lightweight, high-performance automation utility built on PyAutoGUI designed to streamline repetitive mouse tasks. It provides a robust framework for creating custom clicker patterns with minimal overhead.

## Features

*   **Precision Targeting:** Use screen-coordinate mapping or image recognition to trigger clicks at exact UI elements.
*   **Customizable Intervals:** Define specific delay patterns between clicks to bypass basic rate-limiting or anti-bot detection.
*   **Multi-Monitor Support:** Seamlessly coordinate movements across extended displays with coordinate normalization.
*   **Safety Interlocks:** Includes a failsafe mechanism that aborts all scripts if the mouse is moved to a corner of the screen.

## Installation

Ensure you have Python 3.8+ installed. Install the package directly via pip:

```bash
pip install pyautogui
git clone https://github.com/Developer/pyautogui-tools-71.git
cd pyautogui-tools-71
```

*Note: If you are on Linux, ensure `python3-tk` and `python3-dev` are installed to support cross-platform display features.*

## Usage

Create a simple script to automate a clicking sequence. The following example demonstrates a rapid-click loop with a configurable delay:

```python
import pyautogui
from pyautogui_tools_71 import Clicker

# Initialize with a 0.5-second interval between clicks
bot = Clicker(interval=0.5)

# Execute 10 clicks at current coordinates
bot.start_sequence(clicks=10)

# Execute clicks at a specific target location
bot.click_at(x=500, y=500)
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is intended for personal automation and testing purposes only. Use responsibly and ensure compliance with the Terms of Service of any target applications.