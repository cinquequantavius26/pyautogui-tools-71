import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "clicks": 1,
    "failsafe": True,
    "hotkey": "f6"
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json") -> None:
        self.filepath = filepath
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            self._save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG
        with open(self.filepath, "r") as f:
            try:
                return {**DEFAULT_CONFIG, **json.load(f)}
            except json.JSONDecodeError:
                return DEFAULT_CONFIG

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str) -> Any:
        return self.data.get(key, DEFAULT_CONFIG.get(key))

config = ConfigLoader()