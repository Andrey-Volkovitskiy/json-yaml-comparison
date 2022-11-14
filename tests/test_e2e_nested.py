import gendiff


def test_nested_my(capsys):
    file_a = 'tests/fixtures/file3'
    file_b = 'tests/fixtures/file4'

    with open('tests/fixtures/result_nested_my.txt', 'r') as context_man:
        desired_result = context_man.read()

    gendiff.main(((file_a + '.json'), (file_b + '.json')))
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''

    gendiff.main(((file_a + '.yaml'), (file_b + '.yaml')))
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''

    gendiff.main(((file_a + '.json'), (file_b + '.yaml')))
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''


def test_nested_hexlet(capsys):
    file_a = 'tests/fixtures/file5'
    file_b = 'tests/fixtures/file6'

    with open('tests/fixtures/result_nested_hexlet.txt', 'r') as context_man:
        desired_result = context_man.read()

    gendiff.main(((file_a + '.json'), (file_b + '.json')))
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''
