from gendiff import diff


def test_flat_with_updated():
    data_before = {'a': 1}
    data_after = {'a': 2}
    difference = diff.generate(data_before, data_after)
    d = difference[0]
    assert d['old_name'] == 'a'
    assert d['new_name'] == 'a'
    assert d['old_value'] == 1
    assert d['new_value'] == 2
    assert d['children'] is None
    assert diff.get_node_type(d) == diff.UPDATED


def test_flat_with_added():
    data_before = {}
    data_after = {'a': 2}
    difference = diff.generate(data_before, data_after)
    d = difference[0]
    assert d['old_name'] is None
    assert d['new_name'] == 'a'
    assert d['old_value'] is None
    assert d['new_value'] == 2
    assert d['children'] is None
    assert diff.get_node_type(d) == diff.ADDED


def test_flat_with_removed():
    data_before = {'a': 1}
    data_after = {}
    difference = diff.generate(data_before, data_after)
    d = difference[0]
    assert d['old_name'] == 'a'
    assert d['new_name'] is None
    assert d['old_value'] == 1
    assert d['new_value'] is None
    assert d['children'] is None
    assert diff.get_node_type(d) == diff.REMOVED


def test_flat_with_unchanged():
    data_before = {'a': 1}
    data_after = {'a': 1}
    difference = diff.generate(data_before, data_after)
    d = difference[0]
    assert d['old_name'] == 'a'
    assert d['new_name'] == 'a'
    assert d['old_value'] == 1
    assert d['new_value'] == 1
    assert d['children'] is None
    assert diff.get_node_type(d) == diff.UNCHANGED


def test_nested_with_both_have_children():
    data_before = {
        'a': {
            'b': 2,
            'c': 3
        }
    }
    data_after = {
        'a': {
            'd': 4
        }
    }
    difference = diff.generate(data_before, data_after)
    d = difference[0]
    assert d['old_name'] == 'a'
    assert d['new_name'] == 'a'
    assert d['old_value'] is None
    assert d['new_value'] is None
    assert diff.get_node_type(d) == diff.BOTH_HAVE_CHILDREN

    child0, child1, child2 = d['children']
    assert child0['old_name'] == 'b'
    assert child0['new_name'] is None
    assert child0['old_value'] == 2
    assert child0['new_value'] is None
    assert diff.get_node_type(child0) == diff.REMOVED

    assert child1['old_name'] == 'c'
    assert child1['new_name'] is None
    assert child1['old_value'] == 3
    assert child1['new_value'] is None
    assert diff.get_node_type(child1) == diff.REMOVED

    assert child2['old_name'] is None
    assert child2['new_name'] == 'd'
    assert child2['old_value'] is None
    assert child2['new_value'] == 4
    assert diff.get_node_type(child2) == diff.ADDED


def test_nested_with_only_one_has_child():
    data_before = {
        'a': 1
    }
    data_after = {
        'a': {
            'b': 2
        }
    }
    difference = diff.generate(data_before, data_after)
    d = difference[0]
    assert d['old_name'] == 'a'
    assert d['new_name'] == 'a'
    assert d['old_value'] == 1
    assert d['new_value'] == {'b': 2}
    assert d['children'] is None
    assert diff.get_node_type(d) == diff.UPDATED
