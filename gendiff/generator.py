from gendiff import diff


def generate_diff(data1, data2):
    common_keys = get_common_keys(data1, data2)
    difference = []
    for key in sorted(list(common_keys)):
        old_name = key if key in data1 else None
        new_name = key if key in data2 else None
        old_value = data1.get(key, None)
        new_value = data2.get(key, None)
        children = None
        diff_item = diff.make(old_name, new_name,
                              old_value, new_value,
                              children)
        difference.append(diff_item)
    return difference


def get_common_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2
