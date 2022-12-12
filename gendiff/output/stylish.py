from gendiff import diff
from gendiff.output.serializing import to_json_style

FULLINDENT = '    '
HALFINDENT = '  '


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
    for item in difference:
        output += add_line(item, depth) + '\n'
    output += FULLINDENT * depth + '}'
    return output


def add_line(diff_item, depth):
    '''Creates output for certain node in difference tree

    Agruments:
        diff_item - certain node in difference tree
        depth - depth of current node in the tree

    Returns:
        ready to print string(s)
    '''
    (old_name, new_name,
        old_value, new_value, children) = diff.get_all(diff_item)

    if diff.get_node_type(diff_item) == "Node had and still has children":
        return (f'{FULLINDENT * (depth + 1)}{old_name}: '
                f'{get_output(children, depth + 1)}')

    if diff.get_node_type(diff_item) == "Node hasn't been changed":
        return (f'{FULLINDENT * (depth + 1)}{old_name}: '
                f'{to_json_style(old_value)}')

    result = []
    if old_name is not None:
        result.append(f'{FULLINDENT * depth}{HALFINDENT}- {old_name}: '
                      f'{add_value(old_value, depth)}')
    if new_name is not None:
        result.append(f'{FULLINDENT * depth}{HALFINDENT}+ {new_name}: '
                      f'{add_value(new_value, depth)}')
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
