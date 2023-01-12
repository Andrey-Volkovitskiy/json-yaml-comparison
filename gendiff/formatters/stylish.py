from gendiff import diff
from gendiff.formatters.serializing import value_to_json

FULLINDENT = ' ' * 4
HALFINDENT = ' ' * 2


def format(difference, depth=0):
    '''Outputs a difference tree in stylish text format

    Agruments:
        difference - tree of differences between two data structures
        depth - depth of current node in the tree

    Returns:
        ready to print multiline string
    '''
    output = '{'
    if len(difference) > 0:
        output += '\n'
    for node in difference:
        output += node_to_str(node, depth) + '\n'
    output += FULLINDENT * depth + '}'
    return output


def node_to_str(node, depth):
    '''Creates output for certain node in difference tree

    Agruments:
        node - certain node in difference tree
        depth - depth of current node in the tree

    Returns:
        ready to print string(s)
    '''

    node_type = diff.get_node_type(node)
    result = []

    if node_type == diff.BOTH_HAVE_CHILDREN:
        result = (f"{FULLINDENT * depth}{FULLINDENT}{node['old_name']}: "
                  f"{format(node['children'], depth + 1)}")

    elif node_type == diff.UNCHANGED:
        result = (f"{FULLINDENT * depth}{FULLINDENT}{node['old_name']}: "
                  f"{value_to_json(node['old_value'])}")

    elif node_type == diff.REMOVED:
        result = (f"{FULLINDENT * depth}{HALFINDENT}- {node['old_name']}: "
                  f"{value_to_str(node['old_value'], depth)}")

    elif node_type == diff.ADDED:
        result = (f"{FULLINDENT * depth}{HALFINDENT}+ {node['new_name']}: "
                  f"{value_to_str(node['new_value'], depth)}")

    elif node_type == diff.UPDATED:
        first_str = (f"{FULLINDENT * depth}{HALFINDENT}- {node['old_name']}"
                     f": {value_to_str(node['old_value'], depth)}")
        scnd_str = (f"{FULLINDENT * depth}{HALFINDENT}+ {node['new_name']}"
                    f": {value_to_str(node['new_value'], depth)}")
        result = first_str + '\n' + scnd_str

    else:
        raise ValueError(f"Node type '{node_type}' is unknown")

    return result


def value_to_str(value, depth):
    '''Creates output for value

    Agruments:
        value - value of current node
        depth - depth of current node

    Returns:
        ready to print string(s)
    '''
    if not isinstance(value, dict):
        return value_to_json(value)
    return dict_to_str(value, depth + 1)


def dict_to_str(dictionary, depth):
    '''Creates output for comlex value (for subtree)

    Agruments:
        dictionary - subtree
        depth - depth of nodes in this subtree

    Returns:
        ready to print multiline string
    '''
    output = '{'
    if len(dictionary) > 0:
        output += '\n'
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if not isinstance(value, dict):
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{value_to_json(value)}' + '\n')
        else:
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{dict_to_str(value, depth + 1)}' + '\n')
    output += FULLINDENT * depth + '}'
    return output
