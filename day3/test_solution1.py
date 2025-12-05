# Unit tests for "solution1.py"
# Test with: "pytest", "pytest test_solution1.py"

import pytest
from solution1 import main, process_item


def test_process_item_empty():
    assert process_item('11') == '11'


@pytest.mark.parametrize(
        'item, expected',
    [
        ('987654321111111', '98'),
        ('811111111111119', '89'),
        ('234234234234278', '78'),
        ('818181911112111', '92'),
    ]
)
def test_fun1_test_input(item, expected):
    assert process_item(item) == expected


def test_main_empty(tmp_path):
    p = tmp_path / 'pytest_input1.txt'
    p.write_text('11')
    assert main(p, debug=True) == 11


def test_main_sample_input(tmp_path):
    p = tmp_path / 'pytest_input1.txt'
    p.write_text('4321\n1234')
    assert main(p, debug=True) == 43 + 34


def test_main_test_input():
    test_file_path = 'test_input1.txt'
    assert main(test_file_path, debug=True) == 357
