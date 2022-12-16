from gendiff import generate_diff


def test_plain(capsys):
    before = 'tests/fixtures/file5'
    after = 'tests/fixtures/file6'

    with open('tests/fixtures/result_plain_format.txt', 'r') as result_file:
        desired_result = result_file.read()

    result = generate_diff(before + '.json', after + '.json',
                           format_name='plain')
    assert result == desired_result
