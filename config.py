import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "clicks": 1,
    "hotkey": "f6"
}

def load_config(filepath: str) -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    if not os.path.exists(filepath):
        return config
    try:
        with open(filepath, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)