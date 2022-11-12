import gendiff


def test_empty(capsys):
    file_0 = 'tests/fixtures/file0.json'
    file_2 = 'tests/fixtures/file2.json'
    gendiff.main((file_0, file_0))
    out, err = capsys.readouterr()
    assert out == '' + '\n'
    assert err == ''

    gendiff.main((file_0, file_2))
    out, err = capsys.readouterr()
    assert out == '''+ host: hexlet.io
+ timeout: 20
+ verbose: True''' + '\n'


def test_flat(capsys):
    file_1 = 'tests/fixtures/file1.json'
    file_2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/result_test_flat.txt', 'r') as context_man:
        desired_result = context_man.read()
        gendiff.main([file_1, file_2])
        out, err = capsys.readouterr()
        assert out == desired_result + '\n'
        assert err == ''
