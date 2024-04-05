import pytest
from main import read_file


def test_get_file_lines_reads_all_lines(prepare_input_file):
    file_path = prepare_input_file
    expected = ['hello\n', 'world\n', 'hello world\n', 'helloworld']
    result = read_file(file_path)
    assert result == expected


def test_get_file_lines_raises_exception_when_file_does_not_exist():
    file_path = 'non_existing_file.txt'
    with pytest.raises(FileNotFoundError):
        read_file(file_path)
