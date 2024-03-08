import json
from json import JSONDecodeError


def is_valid_json(data: str) -> bool:
    try:
        json.loads(data)
        return True
    except JSONDecodeError:
        return False


def format_json(data: str) -> str:
    loaded_data = json.loads(data)
    return json.dumps(loaded_data, indent=2, separators=(',', ': '))


def minimize_json(data: str) -> str:
    loaded_data = json.loads(data)
    result = json.dumps(loaded_data, separators=(',', ':'))
    return result
