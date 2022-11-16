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
        with open(path_to_file) as content_manager:
            data = parse_json(content_manager)
    elif path_to_file.endswith(('.yaml', '.yml')):
        with open(path_to_file) as content_manager:
            data = parse_yaml(content_manager)
    else:
        raise NameError(f'File "{path_to_file}" have to be .json or .yaml')
    return data


def parse_json(content_manager):
    '''Parse JSON content'''
    return json.load(content_manager)


def parse_yaml(content_manager):
    '''Parse YAML content'''
    data = yaml.safe_load(content_manager)
    if data is None:
        data = {}
    return data
