from gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
FILE3 = 'tests/fixtures/file3'
FILE4 = 'tests/fixtures/file4'


@pytest.mark.parametrize("file1, file2, expected", [
    (FILE3 + '.json', FILE4 + '.json', 'result_nested_my.txt'),
    (FILE3 + '.yaml', FILE4 + '.yaml', 'result_nested_my.txt'),
    (FILE3 + '.json', FILE4 + '.yaml', 'result_nested_my.txt')])
def test_nested_with_my_data(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2) == expected_result


def test_nested_with_hexlet_data():
    file5 = 'tests/fixtures/file5'
    file6 = 'tests/fixtures/file6'
    with open(PATH + 'result_nested_hexlet.txt', 'r') as expected_file:
        expected_result = expected_file.read()
    result = generate_diff(file5 + '.json', file6 + '.json')
    assert result == expected_result
