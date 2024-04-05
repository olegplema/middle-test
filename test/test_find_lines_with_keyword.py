import pytest

from main import find_lines_with_keyword


@pytest.mark.parametrize('input_data, keyword, expected', [
    ([], 'test', []),
    ([''], 'test', []),
    (['hello', 'world', 'hello world', 'helloworld'], 'hello', ['hello', 'hello world', 'helloworld']),
    (['hello', 'world', 'hello world', 'helloworld'], 'test', []),
    (['hello', 'world', 'hello world', 'helloworld'], '', ['hello', 'world', 'hello world', 'helloworld']),
])
def test_get_filtered_lines_returns(input_data: list[str], keyword: str, expected: list[str]):
    result = find_lines_with_keyword(input_data, keyword)
    assert result == expected
