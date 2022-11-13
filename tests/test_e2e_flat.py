import gendiff


def test_empty(capsys):
    file_a = 'tests/fixtures/file0'

    gendiff.main(((file_a + '.json'), (file_a + '.json')))
    out, err = capsys.readouterr()
    assert out == '{}' + '\n'
    assert err == ''

    gendiff.main(((file_a + '.yml'), (file_a + '.yaml')))
    out, err = capsys.readouterr()
    assert out == '{}' + '\n'
    assert err == ''


def test_half_empty(capsys):
    file_a = 'tests/fixtures/file0'
    file_b = 'tests/fixtures/file2'

    with open('tests/fixtures/result_half_empty.txt', 'r') as context_man:
        desired_result = context_man.read()

    gendiff.main(((file_a + '.json'), (file_b + '.json')))
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''

    gendiff.main(((file_a + '.yaml'), (file_b + '.yaml')))
    out, err = capsys.readouterr()
    assert out == desired_result + '\n'
    assert err == ''


def test_flat(capsys):
    file_a = 'tests/fixtures/file1'
    file_b = 'tests/fixtures/file2'

    with open('tests/fixtures/result_flat.txt', 'r') as context_man:
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
