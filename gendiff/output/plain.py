from gendiff import diff
from gendiff.output.serializing import to_json_style


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

        if diff.get_node_type(item) == "Node had and still has children":
            output.append(get_output(children, current_path))
            continue

        old_str_value = val_to_str(old_value)
        new_str_value = val_to_str(new_value)

        if old_name is not None and new_name is None:
            output.append(f"Property '{current_path}' was removed")
            continue

        elif new_name is not None and old_name is None:
            output.append(f"Property '{current_path}' was added "
                          f"with value: {new_str_value}")

        elif old_value != new_value:
            output.append(f"Property '{current_path}' was updated. "
                          f"From {old_str_value} to {new_str_value}")

    return '\n'.join(output)


def val_to_str(value):
    '''Prepares value for output in correct format

    Agruments:
        value - property value

    Returns:
        ready to print string
    '''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{to_json_style(value)}'"
    else:
        return to_json_style(value)
