import argparse
import json
import yaml
from gendiff import diff


def main(test_args=None):
    args = parse_prompt(test_args)
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)
    difference = diff.generate_diff(data1, data2)
    diff_output(difference)


def parse_prompt(test_args):
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args(test_args)
    return args


def parse_file(path_to_file):
    if path_to_file.endswith('.json'):
        with open(path_to_file) as content_manager:
            data = parse_json(content_manager)
    elif path_to_file.endswith(('.yaml', '.yml')):
        with open(path_to_file) as content_manager:
            data = parse_yaml(content_manager)
    else:
        raise NameError(f'File "{path_to_file}" have to be .json or .yaml')
    return data


def parse_json(content_manager):
    return json.load(content_manager)


def parse_yaml(content_manager):
    data = yaml.safe_load(content_manager)
    if data is None:
        data = {}
    return data


def diff_output(difference):
    if len(difference) != 0:
        output = '{\n' + '\n'.join(difference) + '\n}'
    else:
        output = '{}'
    print(output)
