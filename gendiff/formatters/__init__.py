'''This package responsible for difference tree output'''
from gendiff.formatters import stylish, plain, json_diff


def get_output(difference, format_name):
    '''Outputs the difference according to the selected format

    Agruments:
        difference - tree of differences between two data structures
        format_name - one of three formats (stylish, plain, json)

    Returns:
        ready to print multiline string
    '''
    if format_name == 'stylish' or format_name is None:
        return stylish.format(difference)
    elif format_name == 'plain':
        return plain.format(difference)
    elif format_name == 'json':
        return json_diff.format(difference)
    else:
        raise ValueError(f'Wrong format key "{format_name}"!')
