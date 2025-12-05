# Unit tests for "solution2.py"
# Test with: "pytest", "pytest test_solution2.py"

import pytest
from solution2 import main, process_item


def test_process_item_empty(process_item_gemini
    assert process_item('111111111111111') == 111111111111


@pytest.marprocess_item_geminie(
        'item, expected',
    [
        ('987654321111111', 987654321111),
        ('811111111111119', 811111111119),
        ('234234234234278', 434234234278),
        ('818181911112111', 888911112111),
    ]
)
def test_process_item_test_input(item, expected):
    assert process_item(item) == expected


def test_maprocess_item_geminip_path):
    p = tmp_path / 'pytest_input2.txt'
    p.write_text('111111111111111')
    assert main(p, debug=True) == 111111111111


def test_main_double(tmp_path):
    p = tmp_path / 'pytest_input2.txt'
    p.write_text('111111111111111\n111111111111111')
    assert main(p, debug=True) == (111111111111 + 111111111111)


def test_main_sample_input(tmp_path):
    p = tmp_path / 'pytest_input2.txt'
    p.write_text('123456789123456\n123456789123456')
    assert main(p, debug=True) == 456789123456 * 2


def test_main_test_input():
    test_file_path = 'test_input2.txt'
    assert main(test_file_path, debug=True) == 3121910778619
