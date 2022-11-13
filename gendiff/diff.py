def make(old_name=None, new_name=None,
         old_value=None, new_value=None,
         children=None):

    if old_name is None and new_name is None:
        raise ValueError("New_name and old_name are both None")

    if (old_name != new_name and old_name is not None and new_name is not None):
        raise ValueError("New_name and old_name isn`t equal")

    if (children is not None and (
            old_value is not None or new_value is not None)):
        raise ValueError("Simultaneously value AND cildren exist")

    return {
        'name': (old_name, new_name),
        'value': (old_value, new_value),
        'children': children
    }


def get_old_name(d):
    return d['name'][0]


def get_new_name(d):
    return d['name'][1]


def get_old_value(d):
    return d['value'][0]


def get_new_value(d):
    return d['value'][1]


def get_children(d):
    return d['children']


def get_all(d):
    return (get_old_name(d),
            get_new_name(d),
            get_old_value(d),
            get_new_value(d),
            get_children(d))
