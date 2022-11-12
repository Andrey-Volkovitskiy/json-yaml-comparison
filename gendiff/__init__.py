import argparse
import json


def parse_prompt():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def get_common_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2


def get_diff_for_key(key, value1, value2):
    if value1 == value2:
        return f'  {key}: {value1}'
    result = []
    if value1 is not None:
        result.append(f'- {key}: {value1}')
    if value2 is not None:
        result.append(f'+ {key}: {value2}')
    return '\n'.join(result)


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1_manager:
        with open(file_path2) as f2_manager:
            config1 = json.load(f1_manager)
            config2 = json.load(f2_manager)
            common_keys = get_common_keys(config1, config2)
            result = []
            for key in sorted(list(common_keys)):
                value1 = config1.get(key, None)
                value2 = config2.get(key, None)
                result.append(get_diff_for_key(key, value1, value2))
            return '\n'.join(result)
