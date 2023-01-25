from gendiff import parser
from gendiff import diff
from gendiff import formatters


def generate_diff(file_path1, file_path2, format_name='stylish'):
    '''Implements high-level package logic (required for Hexlet tests)

    Agruments:
        file_path1 - first file to compare
        file_path2 - second file to compare
        format_name - format of output (stylish [default], plain, json)

    Returns:
        the difference between file1 and file2 using certain format
    '''
    data1 = parser.get_file_data(file_path1)
    data2 = parser.get_file_data(file_path2)
    difference = diff.generate(data1, data2)
    return formatters.get_output(difference, format_name)
