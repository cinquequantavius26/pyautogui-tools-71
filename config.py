import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "clicks": 1,
    "failsafe": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    if not os.path.exists(filepath):
        _save_default(filepath)
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def _save_default(filepath: str) -> None:
    try:
        with open(filepath, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    except IOError:
        pass