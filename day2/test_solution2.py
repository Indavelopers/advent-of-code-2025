import pytest
from solution2 import load_input, find_invalid_ids, main


def test_load_input(tmp_path):
    """
    Tests that load_input correctly reads a comma-separated file
    and returns a list of strings.
    """
    # Create a temporary file with test data
    p = tmp_path / "pytest_input.txt"
    p.write_text("1-5,10-20,30-35")

    expected = ["1-5", "10-20", "30-35"]
    assert load_input(p) == expected


def test_load_input_with_whitespace(tmp_path):
    """
    Tests that load_input correctly handles leading/trailing whitespace
    in the input file.
    """
    p = tmp_path / "pytest_input.txt"
    p.write_text("  1-5, 10-20 , 30-35 \n, 40-45 ")

    expected = ["1-5", "10-20", "30-35", "40-45"]
    assert load_input(p) == expected


def test_find_invalid_ids_empty():
    """Tests the placeholder find_invalid_ids function returns an empty list."""
    assert find_invalid_ids("1-10") == []


def test_main_function_empty(tmp_path):
    """Tests that the main function returns the correct sum (currently 0)."""
    p = tmp_path / "pytest_input.txt"
    p.write_text("1-5,14-20")
    # Since find_invalid_ids is a stub returning [], the sum should be 0.
    assert main(p) == 0

@pytest.mark.parametrize(
        "id_range, expected",
    [
        ('11-22', [11,22]),
        ('95-115', [99, 111]),
        ('998-1012', [999, 1010]),
        ('1188511880-1188511890', [1188511885]),
        ('222220-222224', [222222]),
        ('1698522-1698528', []),
        ('446443-446449', [446446]),
        ('38593856-38593862', [38593859]),
        ('565653-565659', [565656]),
        ('824824821-824824827', [824824824]),
        ('2121212118-2121212124', [2121212121])
    ]
)
def test_find_invalid_ids_test_input(id_range, expected):
    # Testing 11 ranges

    assert find_invalid_ids(id_range) == expected

# Test test_input.txt to return 4174379265
def test_main_function_test_input():
    test_file_path = 'test_input1.txt'
    assert main(test_file_path) == 4174379265
