from gendiff import diff
import pytest


def test_positional_args():
    d1 = diff.make('a', 'a', 1, 2, None)
    assert diff.get_old_name(d1) == 'a'
    assert diff.get_new_name(d1) == 'a'
    assert diff.get_old_value(d1) == 1
    assert diff.get_new_value(d1) == 2
    assert diff.get_children(d1) is None


def test_keyword_args():
    d1 = diff.make(new_name='b', new_value=2)
    assert diff.get_old_name(d1) is None
    assert diff.get_new_name(d1) == 'b'
    assert diff.get_old_value(d1) is None
    assert diff.get_new_value(d1) == 2
    assert diff.get_children(d1) is None


def test_nested():
    d1 = diff.make('a', 'a', 1, 2, None)
    d2 = diff.make('b', 'b', None, None, [d1])
    d3 = diff.make('c', 'c', None, None, [d1, d2])
    r1, r2 = diff.get_children(d3)
    assert diff.get_old_name(r1) == 'a'
    assert diff.get_new_name(r2) == 'b'
    assert diff.get_old_value(r1) == 1
    assert diff.get_new_value(r2) is None
    assert diff.get_children(r1) is None
    assert diff.get_children(r2) == [d1]


def test_invariants():
    with pytest.raises(Exception):
        diff.make(None, None, 1, 2, None)  # No key

    with pytest.raises(Exception):
        diff.make('a', 'b', 1, 1, None)  # Key changed

    with pytest.raises(Exception):
        diff.make('a', 'a', 1, 2, ['b', 'c'])  # Value AND cildren exist

    with pytest.raises(Exception):
        diff.make('a', 'a', 1, None, ['b', 'c'])  # Value AND cildren exist

    with pytest.raises(Exception):
        diff.make('a', 'a', None, 2, ['b', 'c'])  # Value AND cildren exist
