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
    for node in difference:
        node_type = diff.get_node_type(node)
        current_path = '.'.join(
            filter(None, [ancestors, node["old_name"] or node["new_name"]])
        )

        old_str_value = val_to_str(node["old_value"])
        new_str_value = val_to_str(node["new_value"])

        if node_type == diff.BOTH_HAVE_CHILDREN:
            output.append(get_output(node["children"], current_path))

        elif node_type == diff.REMOVED:
            output.append(f"Property '{current_path}' was removed")

        elif node_type == diff.ADDED:
            output.append(f"Property '{current_path}' was added "
                          f"with value: {new_str_value}")

        elif node_type == diff.UPDATED:
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
