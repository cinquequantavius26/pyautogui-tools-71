import json
import os
from typing import Dict, Any, Optional

def load_click_config(filepath: str) -> Dict[str, Any]:
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "clicks": 1}
    with open(filepath, "r") as f:
        return json.load(f)

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def validate_coords(data: Dict[str, Any]) -> bool:
    x = data.get("x")
    y = data.get("y")
    return isinstance(x, (int, float)) and isinstance(y, (int, float))

def format_click_payload(x: int, y: int, button: str = "left") -> Dict[str, Any]:
    return {
        "x": x,
        "y": y,
        "button": button,
        "timestamp": __import__("time").time()
    }