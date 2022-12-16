from gendiff import diff
import pytest


def test_positional_args():
    d = diff.make('a', 'a', 1, 2, None)
    assert d['old_name'] == 'a'
    assert d['new_name'] == 'a'
    assert d['old_value'] == 1
    assert d['new_value'] == 2
    assert d['children'] is None


def test_keyword_args():
    d = diff.make(new_name='b', new_value=2)
    assert d['old_name'] is None
    assert d['new_name'] == 'b'
    assert d['old_value'] is None
    assert d['new_value'] == 2
    assert d['children'] is None


def test_nested():
    d1 = diff.make('a', 'a', 1, 2, None)
    d2 = diff.make('b', 'b', None, None, [d1])
    d3 = diff.make('c', 'c', None, None, [d1, d2])
    child1, child2 = d3['children']
    assert child1['old_name'] == 'a'
    assert child2['new_name'] == 'b'
    assert child1['old_value'] == 1
    assert child2['new_value'] is None
    assert child1['children'] is None
    assert child2['children'] == [d1]


def test_invariants():
    with pytest.raises(ValueError):
        diff.make(None, None, 1, 2, None)  # No key

    with pytest.raises(ValueError):
        diff.make('a', 'b', 1, 1, None)  # Key changed

    with pytest.raises(ValueError):
        diff.make('a', 'a', 1, 2, ['b', 'c'])  # Value AND cildren exist

    with pytest.raises(ValueError):
        diff.make('a', 'a', 1, None, ['b', 'c'])  # Value AND cildren exist

    with pytest.raises(ValueError):
        diff.make('a', 'a', None, 2, ['b', 'c'])  # Value AND cildren exist
