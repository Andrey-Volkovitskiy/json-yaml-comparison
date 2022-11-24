'''The module with data abstraction'''


def make(old_name=None, new_name=None,
         old_value=None, new_value=None,
         children=None):
    '''Creates tree node describing difference between old and new property
            in cofig file

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

    if (old_name != new_name and old_name is not None and new_name is not None):
        raise ValueError("New_name and old_name aren`t equal")

    if (children is not None and (
            old_value is not None or new_value is not None)):
        raise ValueError("Simultaneously value AND cildren exist")

    return {
        'name': (old_name, new_name),
        'value': (old_value, new_value),
        'children': children
    }


def get_old_name(d):
    '''Gets old property name'''
    return d['name'][0]


def get_new_name(d):
    '''Gets new property name'''
    return d['name'][1]


def get_old_value(d):
    '''Gets old property value'''
    return d['value'][0]


def get_new_value(d):
    '''Gets new property value'''
    return d['value'][1]


def get_children(d):
    '''Gets list of property`s children (list of subnodes)'''
    return d['children']


def get_all(d):
    '''Gets tuple with all property attributes'''
    return (get_old_name(d),
            get_new_name(d),
            get_old_value(d),
            get_new_value(d),
            get_children(d))
