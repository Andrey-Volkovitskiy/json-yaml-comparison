'''This module responsibel for files read and parse'''
import json
import yaml


def get_file_data(path_to_file):
    '''Gets parsed data stucture extracted from the file

    Agruments:
        path_to_file - path to file to read and parse

    Returns:
        extracted data structure
    '''
    if path_to_file.endswith('.json'):
        content_type = 'json'
    elif path_to_file.endswith(('.yaml', '.yml')):
        content_type = 'yaml'
    else:
        raise NameError(f'File "{path_to_file}" have to be .json or .yaml')

    with open(path_to_file) as the_file:
        data = parse_content(the_file, content_type)
    return data


def parse_content(file_content, content_type):
    '''Parse JSON or YAML file content

    Agruments:
        file_content - the content extracted from a configuration file
        content_type - JSON or YAML (depends on the file extension)

    Returns:
        extracted data structure
    '''
    if content_type == 'json':
        return json.load(file_content)
    elif content_type == 'yaml':
        data = yaml.safe_load(file_content)
        return data or {}
    else:
        raise NameError(f'File extention "{content_type}" '
                        f'have to be .json or .yaml')
