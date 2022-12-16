from gendiff import diff
from gendiff.output.serializing import to_json_style

FULLINDENT = ' ' * 4
HALFINDENT = ' ' * 2


def get_output(difference, depth=0):
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
        output += add_line(node, depth) + '\n'
    output += FULLINDENT * depth + '}'
    return output


def add_line(node, depth):
    '''Creates output for certain node in difference tree

    Agruments:
        node - certain node in difference tree
        depth - depth of current node in the tree

    Returns:
        ready to print string(s)
    '''

    node_type = diff.get_node_type(node)

    if node_type == diff.BOTH_HAVE_CHILDREN:
        return (f"{FULLINDENT * (depth + 1)}{node['old_name']}: "
                f"{get_output(node['children'], depth + 1)}")

    if node_type == diff.UNCHANGED:
        return (f"{FULLINDENT * (depth + 1)}{node['old_name']}: "
                f"{to_json_style(node['old_value'])}")

    result = []
    if node_type == diff.REMOVED or node_type == diff.UPDATED:
        result.append(f"{FULLINDENT * depth}{HALFINDENT}- {node['old_name']}: "
                      f"{add_value(node['old_value'], depth)}")
    if node_type == diff.ADDED or node_type == diff.UPDATED:
        result.append(f"{FULLINDENT * depth}{HALFINDENT}+ {node['new_name']}: "
                      f"{add_value(node['new_value'], depth)}")
    return '\n'.join(result)


def add_value(value, depth):
    '''Creates output for value

    Agruments:
        value - value of current node
        depth - depth of current node

    Returns:
        ready to print string(s)
    '''
    if not isinstance(value, dict):
        return to_json_style(value)
    return output_complex_value(value, depth + 1)


def output_complex_value(dictionary, depth):
    '''Creates output for comlex value (for subtree)

    Agruments:
        dictionary - subtree
        depth - depth of nodes in this subtree

    Returns:
        ready to print miltiline string
    '''
    output = '{'
    if len(dictionary) > 0:
        output += '\n'
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if not isinstance(value, dict):
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{to_json_style(value)}' + '\n')
        else:
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{output_complex_value(value, depth + 1)}' + '\n')
    output += FULLINDENT * depth + '}'
    return output
