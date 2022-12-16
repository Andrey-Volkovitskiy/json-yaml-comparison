'''The module with data abstraction'''

ADDED = "added"
UNCHANGED = "unchanged"
REMOVED = "removed"
UPDATED = "updated"
BOTH_HAVE_CHILDREN = "both_has_children"


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


def make(old_name=None, new_name=None,
         old_value=None, new_value=None,
         children=None):
    '''Creates tree node describing difference between the property
            mentioned in old and new cofig file

    Agruments:
        old_name - old property name
        new_name - new property name
        old_value - old property value
        new_value - new property value
        children - list of subnodes (exists only if both values are None)

    Returns:
        tree node (data abstraction)
    '''

    if old_name is None and new_name is None:
        raise ValueError("New_name and old_name are both None")

    if old_name != new_name and old_name is not None and new_name is not None:
        raise ValueError("New_name and old_name aren`t equal")

    if children is not None and \
            (old_value is not None or new_value is not None):
        raise ValueError("Simultaneously value AND cildren exist")

    return {
        'old_name': old_name,
        'new_name': new_name,
        'old_value': old_value,
        'new_value': new_value,
        'children': children
    }
