from gendiff import diff
from gendiff.output.change_value_fomat import to_json


def get_output(difference, ancestors=None):
    '''Outputs a difference tree in plain text format

    Agruments:
        difference - tree of differences between two data structures
        ancestors - path to current node

    Returns:
        ready to print multiline string
    '''
    output = []
    for item in difference:
        (old_name, new_name,
         old_value, new_value, children) = diff.get_all(item)

        current_path = '.'.join(filter(None, [ancestors, old_name or new_name]))

        if new_name == old_name and new_value is old_value is None:
            output.append(get_output(children, current_path))
            continue

        old_mod_value = modify(old_value)
        new_mod_value = modify(new_value)

        if old_name is not None and new_name is None:
            output.append(f"Property '{current_path}' was removed")
            continue

        elif new_name is not None and old_name is None:
            output.append(f"Property '{current_path}' was added "
                          f"with value: {new_mod_value}")

        elif old_value != new_value:
            output.append(f"Property '{current_path}' was updated. "
                          f"From {old_mod_value} to {new_mod_value}")

    return '\n'.join(output)


def modify(value):
    '''Prepares value for output in correct format

    Agruments:
        value - property value

    Returns:
        ready to print string
    '''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{to_json(value)}'"
    else:
        return to_json(value)
