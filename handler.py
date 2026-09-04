import json
import logging
from typing import Any, Dict
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('pyautogui-tools-71')

class ClickDataHandler:
    def __init__(self, filepath: str = 'clicks.json'):
        self.path = Path(filepath)

    def save(self, data: Dict[str, Any]) -> bool:
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return True
        except (IOError, TypeError) as e:
            logger.error(f'failed to save data: {e}')
            return False

    def load(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {}
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f'failed to load data: {e}')
            return {}

    def update_position(self, x: int, y: int, interval: float) -> bool:
        data = self.load()
        data.update({'last_x': x, 'last_y': y, 'interval': interval})
        return self.save(data)