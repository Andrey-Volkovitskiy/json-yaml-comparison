from gendiff import generate_diff


def test_empty():
    file_0 = 'gendiff/tests/file0.json'
    file_2 = 'gendiff/tests/file2.json'
    assert generate_diff(file_0, file_0) == ''
    assert generate_diff(file_0, file_2) == '''+ host: hexlet.io
+ timeout: 20
+ verbose: True'''


def test_flat():
    file_1 = 'gendiff/tests/file1.json'
    file_2 = 'gendiff/tests/file2.json'
    assert generate_diff(file_1, file_2) == '''- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True'''
