import json


def to_json(value):
    '''Prepares internal Python data for output according to JSON:
    None -> null
    True, False -> true, false
    str -> str (remains unchanged)
    '''
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    else:
        return value
