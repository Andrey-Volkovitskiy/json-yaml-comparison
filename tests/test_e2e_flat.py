from gendiff import generate_diff


def test_with_empty():
    before = 'tests/fixtures/file0'

    result = generate_diff(before + '.json', before + '.json')
    assert result == '{}'

    result = generate_diff(before + '.yml', before + '.yaml')
    assert result == '{}'


def test_with_half_empty():
    before = 'tests/fixtures/file0'
    after = 'tests/fixtures/file2'

    with open('tests/fixtures/result_half_empty.txt', 'r') as result_file:
        desired_result = result_file.read()

    result = generate_diff(before + '.json', after + '.json')
    assert result == desired_result

    result = generate_diff(before + '.yaml', after + '.yaml')
    assert result == desired_result


def test_with_flat():
    before = 'tests/fixtures/file1'
    after = 'tests/fixtures/file2'

    with open('tests/fixtures/result_flat.txt', 'r') as result_file:
        desired_result = result_file.read()

    result = generate_diff(before + '.json', after + '.json')
    assert result == desired_result

    result = generate_diff(before + '.yaml', after + '.yaml')
    assert result == desired_result

    result = generate_diff(before + '.json', after + '.yaml')
    assert result == desired_result
