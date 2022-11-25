from gendiff import generate_diff


def test_empty():
    file_a = 'tests/fixtures/file0'

    result = generate_diff(file_a + '.json', file_a + '.json')
    assert result == '{}'

    result = generate_diff(file_a + '.yml', file_a + '.yaml')
    assert result == '{}'


def test_half_empty():
    file_a = 'tests/fixtures/file0'
    file_b = 'tests/fixtures/file2'

    with open('tests/fixtures/result_half_empty.txt', 'r') as context_man:
        desired_result = context_man.read()

    result = generate_diff(file_a + '.json', file_b + '.json')
    assert result == desired_result

    result = generate_diff(file_a + '.yaml', file_b + '.yaml')
    assert result == desired_result


def test_flat(capsys):
    file_a = 'tests/fixtures/file1'
    file_b = 'tests/fixtures/file2'

    with open('tests/fixtures/result_flat.txt', 'r') as context_man:
        desired_result = context_man.read()

    result = generate_diff(file_a + '.json', file_b + '.json')
    assert result == desired_result

    result = generate_diff(file_a + '.yaml', file_b + '.yaml')
    assert result == desired_result

    result = generate_diff(file_a + '.json', file_b + '.yaml')
    assert result == desired_result
