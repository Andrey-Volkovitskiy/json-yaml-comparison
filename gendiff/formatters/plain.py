from gendiff import diff
from gendiff.formatters.serializing import value_to_json


def format(difference, ancestors=None):
    '''Prepares a difference tree for output in plain text format

    Agruments:
        difference - tree of differences between two data structures
        ancestors - path to current node

    Returns:
        ready to print multiline string
    '''
    result = []
    for node in difference:
        node_type = diff.get_node_type(node)
        current_path = '.'.join(
            filter(None, [ancestors, node["old_name"] or node["new_name"]])
        )
        old_value_str = val_to_str(node["old_value"])
        new_value_str = val_to_str(node["new_value"])

        match node_type:
            case diff.BOTH_HAVE_CHILDREN:
                result.append(format(node["children"], current_path))

            case diff.REMOVED:
                result.append(f"Property '{current_path}' was removed")

            case diff.ADDED:
                result.append(f"Property '{current_path}' was added "
                              f"with value: {new_value_str}")

            case diff.UPDATED:
                result.append(f"Property '{current_path}' was updated. "
                              f"From {old_value_str} to {new_value_str}")
            
            case diff.UNCHANGED:
                pass

            case _:
                raise ValueError(f"Node type '{node_type}' is unknown")

    return '\n'.join(result)


def val_to_str(value):
    '''Prepares value for result in correct format

    Agruments:
        value - property value

    Returns:
        ready to print string
    '''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value_to_json(value)}'"
    else:
        return value_to_json(value)
