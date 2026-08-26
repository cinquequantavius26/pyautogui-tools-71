import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "clicks_per_second": 10,
    "button": "left",
    "hold_duration": 0.01,
    "toggle_key": "F6"
}

def load_clicker_profile(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_clicker_profile(filepath: str, config: Dict[str, Any]) -> bool:
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(cps: float) -> float:
    if cps <= 0:
        return 0.1
    return 1.0 / float(cps)
