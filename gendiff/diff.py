def generate_diff(data1, data2):
    common_keys = get_common_keys(data1, data2)
    difference = []
    for key in sorted(list(common_keys)):
        value1 = data1.get(key, None)
        value2 = data2.get(key, None)
        difference.append(get_diff_for_key(key, value1, value2))
    return difference


def get_common_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2


def get_diff_for_key(key, value1, value2):
    if value1 == value2:
        return f'  {key}: {value1}'
    result = []
    indent = '  '
    if value1 is not None:
        result.append(f'{indent}- {key}: {value1}')
    if value2 is not None:
        result.append(f'{indent}+ {key}: {value2}')
    return '\n'.join(result)
