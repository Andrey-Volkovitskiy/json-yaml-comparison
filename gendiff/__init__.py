import argparse
from gendiff import parser
from gendiff import generator
from gendiff import output


def main(test_args=None):
    args = parse_prompt(test_args)
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parser.parse_file(file_path1)
    data2 = parser.parse_file(file_path2)
    difference = generator.generate_diff(data1, data2)
    return output.output_diff(difference, format_name)


def parse_prompt(test_args):
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args(test_args)
    return args
