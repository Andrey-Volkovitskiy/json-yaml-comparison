from gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
FILE0 = 'tests/fixtures/file0'

FILE1 = 'tests/fixtures/file1'
FILE2 = 'tests/fixtures/file2'


@pytest.mark.parametrize("file1, file2, expected", [
    (FILE0 + '.json', FILE0 + '.json', '{}'),
    (FILE0 + '.yml', FILE0 + '.yaml', '{}'),])
def test_with_empty(file1, file2, expected):
    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize("file1, file2, expected", [
    (FILE0 + '.json', FILE2 + '.json', 'result_half_empty.txt'),
    (FILE0 + '.yml', FILE2 + '.yaml', 'result_half_empty.txt'),])
def test_with_half_empty(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2) == expected_result


@pytest.mark.parametrize("file1, file2, expected", [
    (FILE1 + '.json', FILE2 + '.json', 'result_flat.txt'),
    (FILE1 + '.yaml', FILE2 + '.yaml', 'result_flat.txt'),])
def test_with_flat(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2) == expected_result
