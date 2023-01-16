from gendiff import generate_diff


def test_plain(capsys):
    file5 = 'tests/fixtures/file5'
    file6 = 'tests/fixtures/file6'

    with open('tests/fixtures/result_plain_format.txt', 'r') as expected_file:
        expected_result = expected_file.read()

    result = generate_diff(file5 + '.json', file6 + '.json',
                           format_name='plain')
    assert result == expected_result
