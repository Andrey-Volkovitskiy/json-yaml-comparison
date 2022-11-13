from gendiff import diff

FULLINDENT = '    '
HALFINDENT = '  '


def print_diff(difference):
    output = '{'
    if len(difference) > 0:
        output += '\n'
    for item in difference:
        output += add_line(item) + '\n'
    output += '}'
    print(output)


def add_line(diff_item):
    (old_name, new_name,
        old_value, new_value, children) = diff.get_all(diff_item)

    if new_name == old_name and new_value == old_value:
        return f'{FULLINDENT}{old_name}: {old_value}'

    result = []
    if old_name is not None:
        result.append(f'{HALFINDENT}- {old_name}: {old_value}')
    if new_name is not None:
        result.append(f'{HALFINDENT}+ {new_name}: {new_value}')
    return '\n'.join(result)
