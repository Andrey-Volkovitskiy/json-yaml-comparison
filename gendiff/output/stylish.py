from gendiff import diff

FULLINDENT = '    '
HALFINDENT = '  '


def get_output(difference, depth=0):
    output = '{'
    if len(difference) > 0:
        output += '\n'
    for item in difference:
        output += add_line(item, depth) + '\n'
    output += FULLINDENT * depth + '}'
    return output


def add_line(diff_item, depth):
    (old_name, new_name,
        old_value, new_value, children) = diff.get_all(diff_item)

    if new_name == old_name and new_value is old_value is None:
        return (f'{FULLINDENT * (depth + 1)}{old_name}: '
                f'{get_output(children, depth + 1)}')

    if new_name == old_name and new_value == old_value:
        return f'{FULLINDENT * (depth + 1)}{old_name}: {old_value}'

    result = []
    if old_name is not None:
        result.append(f'{FULLINDENT * depth}{HALFINDENT}- {old_name}: '
                      f'{add_value(old_value, depth)}')
    if new_name is not None:
        result.append(f'{FULLINDENT * depth}{HALFINDENT}+ {new_name}: '
                      f'{add_value(new_value, depth)}')
    return '\n'.join(result)


def add_value(value, depth):
    if not isinstance(value, dict):
        return value
    return output_complex_value(value, depth + 1)


def output_complex_value(dictionary, depth):
    output = '{'
    if len(dictionary) > 0:
        output += '\n'
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if not isinstance(value, dict):
            output += f'{FULLINDENT * (depth + 1)}{key}: {value}' + '\n'
        else:
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{output_complex_value(value, depth + 1)}' + '\n')
    output += FULLINDENT * depth + '}'
    return output
