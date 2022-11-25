#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def parse_prompt():
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
    args = parser.parse_args()
    return args


def main():
    '''Prints difference between two JSON or YAML files

    Agruments:
        test_args - gets (path_to_file1, path_to_file2, opional_format_key) from
            Pytest tests or input from user

    Returns:
        prints the difference between file1 and file2 using one of three formats
    '''
    args = parse_prompt()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
