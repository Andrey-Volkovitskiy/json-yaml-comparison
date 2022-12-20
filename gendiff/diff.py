'''The module with data abstraction'''


def generate(data1, data2):
    '''The function responsibel for creation of the tree
    which describes the difference between two data structures

    Agruments:
        data1 - dict parsed from 1st JSON/YAML file
        data2 - dict parsed from 2nd JSON/YAML file

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

        if type(val1) == type(val2) == dict:  # Both nodes HAVE_CHILDREN
            old_value = None
            new_value = None
            children = generate(val1, val2)
        else:                     # At least one node hasn't children
            old_value = val1
            new_value = val2
            children = None

        diff_node = {
            'old_name': old_name,
            'new_name': new_name,
            'old_value': old_value,
            'new_value': new_value,
            'children': children
        }
        difference.append(diff_node)
    return difference


def get_all_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2


# Possible types of diff_node:
ADDED = "added"
UNCHANGED = "unchanged"
REMOVED = "removed"
UPDATED = "updated"
BOTH_HAVE_CHILDREN = "both_have_children"


def get_node_type(d):
    '''Gets type of the node'''

    if d["old_name"] is None and d["old_value"] is None and \
            d["new_value"] is not None and d["new_name"] is not None:
        return ADDED

    elif d["old_name"] == d["new_name"] and \
            d["old_value"] == d["new_value"] is not None:
        return UNCHANGED

    elif d["old_value"] is not None and d["old_name"] is not None and \
            d["new_name"] is None and d["new_value"] is None:
        return REMOVED

    elif d["old_name"] == d["new_name"] and d["old_value"] != d["new_value"]:
        return UPDATED

    elif d["children"]:
        return BOTH_HAVE_CHILDREN

    else:
        raise ValueError(f"Unable to determine type of {d}")
