import argparse
from gendiff import parser
from gendiff import generator
from gendiff import output


def main(test_args=None):
    '''Prints difference between two JSON or YAML files

    Agruments:
        test_args - gets (path_to_file1, path_to_file2, opional_format_key) from
            Pytest tests or input from user

    Returns:
        prints the difference between file1 and file2 using one of three formats
    '''
    args = parse_prompt(test_args)
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    '''Implements high-level package logic (required for Hexlet tests)

    Agruments:
        file_path1 - first file to compare
        file_path1 - second file to compare
        format_name - format of output (stylish [default], plain, json)

    Returns:
        the difference between file1 and file2 using certain format
    '''
    data1 = parser.parse_file(file_path1)
    data2 = parser.parse_file(file_path2)
    difference = generator.generate_diff(data1, data2)
    return output.output_diff(difference, format_name)


def parse_prompt(test_args):
    '''Gets input from user as gendiff aruments

    Agruments:
        file_path1 - first file to compare
        file_path1 - second file to compare
        [format_name] - optional format of output

    Returns:
        tuple with three arguments given by the user
    '''
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args(test_args)
    return args
