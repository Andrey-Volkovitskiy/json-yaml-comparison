from gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
FILE0 = 'tests/fixtures/file0'

FILE1 = 'tests/fixtures/file1'
FILE2 = 'tests/fixtures/file2'


@pytest.mark.parametrize("file1, file2, expected", [
    (f"{FILE0}.json", f"{FILE0}.json", '{}'),
    (f"{FILE0}.yml", f"{FILE0}.yaml", '{}')])
def test_with_empty(file1, file2, expected):
    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize("file1, file2, expected", [
    (f'{FILE0}.json', f'{FILE2}.json', 'result_half_empty.txt'),
    (f'{FILE0}.yml', f'{FILE2}.yaml', 'result_half_empty.txt')])
def test_with_half_empty(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2) == expected_result


@pytest.mark.parametrize("file1, file2, expected", [
    (f'{FILE1}.json', f'{FILE2}.json', 'result_flat.txt'),
    (f'{FILE1}.yaml', f'{FILE2}.yaml', 'result_flat.txt')])
def test_with_flat(file1, file2, expected):
    with open(PATH + expected, 'r') as expected_file:
        expected_result = expected_file.read()
    assert generate_diff(file1, file2) == expected_result
