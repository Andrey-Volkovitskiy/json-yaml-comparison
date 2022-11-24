'''This module responsibel for files read and parse'''
import json
import yaml


def parse_file(path_to_file):
    '''Parse JSON or YAML input file

    Agruments:
        path_to_file - path to file to read and parse

    Returns:
        extracted data structure
    '''
    if path_to_file.endswith('.json'):
        with open(path_to_file) as the_file:
            data = parse_json(the_file)
    elif path_to_file.endswith(('.yaml', '.yml')):
        with open(path_to_file) as the_file:
            data = parse_yaml(the_file)
    else:
        raise NameError(f'File "{path_to_file}" have to be .json or .yaml')
    return data


def parse_json(the_file):
    '''Parse JSON content'''
    return json.load(the_file)


def parse_yaml(the_file):
    '''Parse YAML content'''
    data = yaml.safe_load(the_file)
    if data is None:
        data = {}
    return data
