def value_to_json(value):
    '''Prepares internal Python data for output according to JSON value naming

    Agruments:
        value - Python internal value

    Returns:
        string according to JSON value naming

    None -> null
    True, False -> true, false
    str -> str (remains unchanged)
    '''
    if value is None:
        result = 'null'
    elif type(value) is bool:
        result = 'true' if value else 'false'
    else:
        result = str(value)
    return result
