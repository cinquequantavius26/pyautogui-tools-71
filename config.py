import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "clicks": 1,
    "failsafe": True
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return DEFAULT_CONFIG
        
        try:
            with open(self.filepath, "r") as f:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def save(self, config: Dict[str, Any]) -> None:
        with open(self.filepath, "w") as f:
            json.dump(config, f, indent=4)