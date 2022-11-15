from gendiff.output import stylish, plain


def output_diff(difference, format):
    if format is None:
        return stylish.get_output(difference)
    elif format == 'plain':
        return plain.get_output(difference)
    else:
        raise SyntaxError(f'Wrong format key "{format}"!')
