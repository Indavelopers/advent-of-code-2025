import pytest
from solution1 import rotate_dial, main, START_DIAL, MAX_POSITIONS


@pytest.mark.parametrize(
    "current_dial, direction, rotations, max_pos, expected",
    [
        # Test 'L' (left) rotations
        (5, "L", 1, 10, 4),  # Simple left rotation
        (4, "L", 5, 10, 9),  # Left rotation with wrap-around
        (0, "L", 1, 10, 9),  # Left rotation from 0
        (6, "L", 10, 10, 6),  # A full rotation to the left
        (6, "L", 12, 10, 4),  # A full rotation to the left + 2

        # Test 'R' (right) rotations
        (5, "R", 1, 10, 6),  # Simple right rotation
        (6, "R", 5, 10, 1),  # Right rotation with wrap-around
        (9, "R", 1, 10, 0),  # Right rotation to 0
        (4, "R", 10, 10, 4),  # A full rotation to the right
        (4, "R", 12, 10, 6),  # A full rotation to the right + 2

        # Test zero rotation
        (5, "L", 0, 10, 5),
        (5, "R", 0, 10, 5),

        # Test with a different max_positions
        (10, "R", 5, 20, 15),
        (2, "L", 5, 20, 17),
    ],
)
def test_rotate_dial(current_dial, direction, rotations, max_pos, expected):
    """Tests the rotate_dial function with various valid inputs."""
    assert rotate_dial(current_dial, direction, rotations, max_pos) == expected

def test_rotate_dial_invalid_direction():
    """Tests that rotate_dial raises a ValueError for an invalid direction."""
    with pytest.raises(ValueError, match="Invalid direction"):
        rotate_dial(5, "X", 10, MAX_POSITIONS)

def test_main_output(capsys):
    """Tests the output of the main function."""
    assert main(start_dial=50, input_file='test_input.csv') == (32, 3)
