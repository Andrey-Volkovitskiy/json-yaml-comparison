'''This module responsibel for creation of the tree
    which describes the difference between two data structures'''
from gendiff import diff


def generate_diff(data1, data2):
    '''Calculates difference between two data structures

    Agruments:
        data1 - 1st dict parsed from JSON/YAML file
        data2 - 2nd dict parsed from JSON/YAML file

    Returns:
        the tree which describes difference between two data structures
    '''
    all_keys = get_all_keys(data1, data2)
    difference = []
    for key in sorted(list(all_keys)):
        old_name = key if key in data1 else None
        new_name = key if key in data2 else None

        val1 = data1.get(key)
        val2 = data2.get(key)

        if type(val1) == type(val2) == dict:  # Both nodes HAS_CHILDREN
            old_value = None
            new_value = None
            children = generate_diff(val1, val2)
        else:                     # At least one node hasn't children
            old_value = val1
            new_value = val2
            children = None

        diff_item = diff.make(
            old_name,
            new_name,
            old_value,
            new_value,
            children
        )
        difference.append(diff_item)
    return difference


def get_all_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2
