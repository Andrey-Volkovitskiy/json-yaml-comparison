import json


def to_json_style(value):
    '''Prepares internal Python data for output according to JSON value naming

    Agruments:
        value - Python internal value

    Returns:
        string according to JSON value naming

    None -> null
    True, False -> true, false
    str -> str (remains unchanged)
    '''
    if value is None or type(value) is bool:
        return json.dumps(value)
    else:
        return value
