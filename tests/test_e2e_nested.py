from gendiff import generate_diff


def test_nested_with_my_data():
    before = 'tests/fixtures/file3'
    after = 'tests/fixtures/file4'

    with open('tests/fixtures/result_nested_my.txt', 'r') as result_file:
        desired_result = result_file.read()

    result = generate_diff(before + '.json', after + '.json')
    assert result == desired_result

    result = generate_diff(before + '.yaml', after + '.yaml')
    assert result == desired_result

    result = generate_diff(before + '.json', after + '.yaml')
    assert result == desired_result


def test_nested_with_hexlet_data():
    before = 'tests/fixtures/file5'
    after = 'tests/fixtures/file6'

    with open('tests/fixtures/result_nested_hexlet.txt', 'r') as result_file:
        desired_result = result_file.read()

    result = generate_diff(before + '.json', after + '.json')
    assert result == desired_result
