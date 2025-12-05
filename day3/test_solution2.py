# Unit tests for "solution2.py"
# Test with: "pytest", "pytest test_solution2.py"

import pytest
from solution2 import main, fun1


def test_fun1_empty():
    assert fun1('') == ''


@pytest.mark.parametrize(
        'arg1, expected',
    [
        ('foo', 'foo'),
    ]
)
def test_fun1_test_input(arg1, expected):
    assert fun1(arg1) == expected


def test_main_empty(tmp_path):
    p = tmp_path / 'pytest_input1.txt'
    p.write_text('')
    assert main(p) == ''


def test_main_sample_input(tmp_path):
    p = tmp_path / 'pytest_input1.txt'
    p.write_text('sample data')
    assert main(p) == 'sample data'


def test_main_test_input():
    test_file_path = 'test_input1.txt'
    assert main(test_file_path) == 'test_input1 - hello world!'
