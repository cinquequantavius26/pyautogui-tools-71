import json
from typing import Dict, Any, Optional

class ClickerDataProcessor:
    """Handles serialization of autoclicker configuration files."""

    @staticmethod
    def load_config(filepath: str) -> Dict[str, Any]:
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_config(filepath: str, data: Dict[str, Any]) -> bool:
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except IOError:
            return False

    @staticmethod
    def validate_params(data: Dict[str, Any]) -> bool:
        required_keys = {'interval', 'button', 'repeats'}
        return all(key in data for key in required_keys)

    def process_sequence(self, sequence: list) -> list:
        return [self._sanitize_step(step) for step in sequence]

    def _sanitize_step(self, step: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'x': int(step.get('x', 0)),
            'y': int(step.get('y', 0)),
            'delay': float(step.get('delay', 0.1))
        }