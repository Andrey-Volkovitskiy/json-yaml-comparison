from gendiff import diff
import json


def get_output(difference):
    '''Outputs a difference tree in JSON format

    Agruments:
        difference - tree of differences between two data structures

    Returns:
        ready to print JSON string
    '''
    prepared_dif = prepare(difference)
    return json.dumps(prepared_dif, sort_keys=False, indent=4)


def prepare(difference):
    '''Converts abstract data to easy readable and transerable form

    Agruments:
        difference - tree of differences between two data structures

    Returns:
        formated tree
    '''
    if not difference:
        return None
    result = []
    for item in difference:
        (old_name, new_name,
         old_value, new_value, children) = diff.get_all(item)
        new_item = {'old_name': old_name,
                    'new_name': new_name,
                    'old_value': old_value,
                    'new_value': new_value,
                    'children': prepare(children)}
        result.append(new_item)
    return result
