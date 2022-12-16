from gendiff import generate_diff


def test_json(capsys):
    before = 'tests/fixtures/file5'
    after = 'tests/fixtures/file6'

    with open('tests/fixtures/result_json_format.json', 'r') as result_file:
        desired_result = result_file.read()

    result = generate_diff(before + '.json', after + '.json',
                           format_name='json')
    assert result == desired_result
