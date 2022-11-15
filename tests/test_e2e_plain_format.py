import gendiff


def test_plain(capsys):
    file_a = 'tests/fixtures/file5'
    file_b = 'tests/fixtures/file6'

    with open('tests/fixtures/result_plain_format.txt', 'r') as context_man:
        desired_result = context_man.read()

    gendiff.main([file_a + '.json', file_b + '.json', '--format', 'plain'])
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''
