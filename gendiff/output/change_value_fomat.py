import json


def to_json(value):
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    else:
        return value
