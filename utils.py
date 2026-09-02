import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class ClickData:
    x: float
    y: float
    delay: float
    button: str = 'left'
    clicks: int = 1

def load_click_data(filepath: str) -> List[ClickData]:
    with open(filepath, 'r') as file:
        raw_data = json.load(file)
    return [ClickData(**item) for item in raw_data]

def save_click_data(filepath: str, data: List[ClickData]) -> None:
    serializable = [asdict(item) for item in data]
    with open(filepath, 'w') as file:
        json.dump(serializable, file, indent=4)

def filter_click_data(data: List[ClickData], min_delay: float = 0.0, max_delay: float = float('inf')) -> List[ClickData]:
    return [item for item in data if min_delay <= item.delay <= max_delay]

def generate_sample_data(count: int = 5) -> List[ClickData]:
    return [ClickData(x=100.0 + i * 50, y=100.0 + i * 50, delay=0.5) for i in range(count)]

def merge_click_data(data1: List[ClickData], data2: List[ClickData]) -> List[ClickData]:
    return data1 + data2

def validate_click_data(data: List[ClickData]) -> bool:
    if not data:
        return False
    for item in data:
        if not isinstance(item, ClickData):
            return False
        if item.button not in ['left', 'right', 'middle']:
            return False
        if item.clicks < 1:
            return False
    return True

def sort_click_data(data: List[ClickData], by: str = 'delay') -> List[ClickData]:
    if by == 'delay':
        return sorted(data, key=lambda x: x.delay)
    elif by == 'x':
        return sorted(data, key=lambda x: x.x)
    elif by == 'y':
        return sorted(data, key=lambda x: x.y)
    return data[:]
