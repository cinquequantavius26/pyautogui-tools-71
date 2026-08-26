import json
import os


DEFAULT_CONFIG = {
    "clicks_per_second": 10.0,
    "button": "left",
    "hotkey": "f6",
    "hold_delay": 0.05,
    "randomize_delay": False,
    "delay_variance": 0.01,
}


def load_config(filepath=None):
    config = DEFAULT_CONFIG.copy()
    
    if filepath and os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    config.update({k: v for k, v in user_config.items() if k in DEFAULT_CONFIG})
        except (json.JSONDecodeError, IOError):
            pass
            
    return config


def save_config(config, filepath):
    final_config = DEFAULT_CONFIG.copy()
    if isinstance(config, dict):
        final_config.update({k: v for k, v in config.items() if k in DEFAULT_CONFIG})
        
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(final_config, f, indent=4)
