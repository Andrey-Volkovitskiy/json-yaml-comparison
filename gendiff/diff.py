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

        both_nodes_have_children = (
            isinstance(val1, dict) and isinstance(val2, dict) )
        if both_nodes_have_children:
            old_value = None
            new_value = None
            children = generate(val1, val2)

        else:
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
        check_invariant(diff_node)
        difference.append(diff_node)
    return difference


def get_all_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2


def check_invariant(diff_node):
    '''Checks diff_node invariants'''

    if diff_node['old_name'] != diff_node['new_name'] and \
            diff_node['old_name'] is not None and \
            diff_node['new_name'] is not None:
        raise ValueError(f"old_name '{diff_node['old_name']} and new_name "
                         f"{diff_node['new_name']} can't be unequal")


# Possible types of diff_node:
ADDED = "added"
REMOVED = "removed"
UNCHANGED = "unchanged"
UPDATED = "updated"
BOTH_HAVE_CHILDREN = "both_have_children"


def get_node_type(d):
    '''Gets type of the node'''

    if d["children"]:
        node_type = BOTH_HAVE_CHILDREN

    elif d["old_name"] is None and d["new_name"] is not None:
        node_type = ADDED

    elif d["old_name"] is not None and d["new_name"] is None:
        node_type = REMOVED

    elif d["old_value"] == d["new_value"]:
        node_type = UNCHANGED

    elif d["old_value"] != d["new_value"]:
        node_type = UPDATED

    else:
        raise ValueError(f"Unable to determine type of {d}")

    return node_type
