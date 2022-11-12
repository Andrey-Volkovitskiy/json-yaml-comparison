from gendiff import generate_diff


def test_empty():
    file_0 = 'tests/fixtures/file0.json'
    file_2 = 'tests/fixtures/file2.json'
    assert generate_diff(file_0, file_0) == ''
    assert generate_diff(file_0, file_2) == '''+ host: hexlet.io
+ timeout: 20
+ verbose: True'''


def test_flat():
    file_1 = 'tests/fixtures/file1.json'
    file_2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/result_test_flat.md', 'r') as context_man:
        desired_result = context_man.read()
        assert generate_diff(file_1, file_2) == desired_result
