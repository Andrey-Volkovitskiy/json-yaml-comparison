'''This package responsible for difference tree output'''
from gendiff.output import stylish, plain, json_diff


def output_diff(difference, format):
    '''Outputs the difference according to the selected format

    Agruments:
        difference - tree of differences between two data structures
        format - one of three formats (stylish, plain, json)

    Returns:
        ready to print multiline string
    '''
    if format == 'stylish' or format is None:
        return stylish.get_output(difference)
    elif format == 'plain':
        return plain.get_output(difference)
    elif format == 'json':
        return json_diff.get_output(difference)
    else:
        raise ValueError(f'Wrong format key "{format}"!')
