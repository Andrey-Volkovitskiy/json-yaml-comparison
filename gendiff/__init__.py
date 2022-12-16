from gendiff import parser
from gendiff import generator
from gendiff import output


def generate_diff(file_path1, file_path2, format_name='stylish'):
    '''Implements high-level package logic (required for Hexlet tests)

    Agruments:
        file_path1 - first file to compare
        file_path2 - second file to compare
        format_name - format of output (stylish [default], plain, json)

    Returns:
        the difference between file1 and file2 using certain format
    '''
    data1 = parser.parse_file(file_path1)
    data2 = parser.parse_file(file_path2)
    difference = generator.generate_diff(data1, data2)
    return output.output_diff(difference, format_name)
