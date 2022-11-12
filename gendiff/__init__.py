import argparse
import json
from gendiff import diff


def parse_json(file_manager):
    return json.load(file_manager)


def diff_output(difference):
    if len(difference) != 0:
        output = '{\n' + '\n'.join(difference) + '\n}'
    else:
        output = '{}'
    print(output)


def parse_prompt(test_args):
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args(test_args)
    return args


def main(test_args=None):
    args = parse_prompt(test_args)
    with open(args.first_file) as f1_manager:
        with open(args.second_file) as f2_manager:
            data1 = parse_json(f1_manager)
            data2 = parse_json(f2_manager)
    difference = diff.generate_diff(data1, data2)
    diff_output(difference)
