from gendiff import generate_diff


def test_json(capsys):
    file_a = 'tests/fixtures/file5'
    file_b = 'tests/fixtures/file6'

    with open('tests/fixtures/result_json_format.json', 'r') as context_man:
        desired_result = context_man.read()

    result = generate_diff(file_a + '.json', file_b + '.json', 'json')
    assert result == desired_result
