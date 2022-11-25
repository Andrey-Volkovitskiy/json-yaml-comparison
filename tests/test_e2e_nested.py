from gendiff import generate_diff


def test_nested_my():
    file_a = 'tests/fixtures/file3'
    file_b = 'tests/fixtures/file4'

    with open('tests/fixtures/result_nested_my.txt', 'r') as context_man:
        desired_result = context_man.read()

    result = generate_diff(file_a + '.json', file_b + '.json')
    assert result == desired_result

    result = generate_diff(file_a + '.yaml', file_b + '.yaml')
    assert result == desired_result

    result = generate_diff(file_a + '.json', file_b + '.yaml')
    assert result == desired_result


def test_nested_hexlet():
    file_a = 'tests/fixtures/file5'
    file_b = 'tests/fixtures/file6'

    with open('tests/fixtures/result_nested_hexlet.txt', 'r') as context_man:
        desired_result = context_man.read()

    result = generate_diff(file_a + '.json', file_b + '.json')
    assert result == desired_result
