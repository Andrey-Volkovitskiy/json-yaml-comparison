import argparse
from gendiff import parser
from gendiff import generator
from gendiff import output


def main(test_args=None):
    args = parse_prompt(test_args)
    data1 = parser.parse_file(args.first_file)
    data2 = parser.parse_file(args.second_file)
    difference = generator.generate_diff(data1, data2)
    print(output.output_diff(difference, args.format))


def parse_prompt(test_args):
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args(test_args)
    return args
