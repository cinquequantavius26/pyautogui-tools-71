import time
from typing import Optional, Dict, Any
import pyautogui

class AutoclickProcessor:
    """Processes automated clicking tasks using pyautogui."""

    def __init__(self, interval: float = 0.5, button: str = "left") -> None:
        """Set up the click processor.

        Args:
            interval: Time between consecutive clicks.
            button: The mouse button to click with.
        """
        self.interval: float = max(0.01, interval)
        self.button: str = button
        self.running: bool = False

    def start(self, duration: Optional[float] = None) -> int:
        """Begin automated clicking.

        Args:
            duration: Maximum time to run in seconds.
        Returns:
            Count of clicks completed.
        """
        self.running = True
        clicks: int = 0
        start_time: float = time.time()
        while self.running:
            pyautogui.click(button=self.button)
            clicks += 1
            if duration is not None and time.time() - start_time >= duration:
                self.running = False
                break
            time.sleep(self.interval)
        return clicks

    def stop(self) -> None:
        """Halt the clicking operation."""
        self.running = False

    def update_settings(self, interval: Optional[float] = None, button: Optional[str] = None) -> None:
        """Modify processor configuration.

        Args:
            interval: New click interval if provided.
            button: New button if provided.
        """
        if interval is not None and interval > 0:
            self.interval = interval
        if button is not None:
            self.button = button

    def get_info(self) -> Dict[str, Any]:
        """Provide current configuration details.

        Returns:
            Status information as dictionary.
        """
        return {
            "running": self.running,
            "interval": self.interval,
            "button": self.button
        }


def create_processor(interval: float = 0.5, button: str = "left") -> AutoclickProcessor:
    """Factory function to instantiate processor.

    Args:
        interval: Click delay.
        button: Click button.
    Returns:
        New AutoclickProcessor instance.
    """
    return AutoclickProcessor(interval=interval, button=button)