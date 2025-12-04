import pytest
from solution2 import rotate_dial, main, START_DIAL, MAX_POSITIONS


@pytest.mark.parametrize(
    "current_dial, direction, rotations, max_pos, expected, zero_dial_counts",
    [
        # Test 'L' (left) rotations
        (5, "L", 1, 10, 4, 0),  # Simple left rotation
        (4, "L", 5, 10, 9, 1),  # Left rotation with wrap-around
        (0, "L", 1, 10, 9, 0),  # Left rotation from 0
        (6, "L", 10, 10, 6, 1),  # A full rotation to the left
        (6, "L", 12, 10, 4, 1),  # A full rotation to the left + 2

        # Test 'R' (right) rotations
        (5, "R", 1, 10, 6, 0),  # Simple right rotation
        (6, "R", 5, 10, 1, 1),  # Right rotation with wrap-around
        (9, "R", 1, 10, 0, 1),  # Right rotation to 0
        (4, "R", 10, 10, 4, 1),  # A full rotation to the right
        (4, "R", 12, 10, 6, 1),  # A full rotation to the right + 2

        # Test zero rotation
        (5, "L", 0, 10, 5, 0),
        (5, "R", 0, 10, 5, 0),

        # Test with a different max_positions
        (10, "R", 5, 20, 15, 0),
        (2, "L", 5, 20, 17, 1),

        # Test 2 wrap-arounds
        (6, "L", 20, 10, 6, 2),  # A full 2 rotations to the left
        (6, "L", 22, 10, 4, 2),  # A full 2 rotations to the left + 2
        (6, "L", 32, 10, 4, 3),  # A full 3 rotations to the left + 2
        (4, "R", 20, 10, 4, 2),  # A full 2 rotations to the right
        (4, "R", 22, 10, 6, 2),  # A full 2 rotations to the right + 2
        (4, "R", 32, 10, 6, 3),  # A full 3 rotations to the right + 2

        # Test "be careful"
        (50, "R", 1000, 100, 50, 10), # Starting at 50, R1000, returns to 50, password 10
        (50, 'L', 1000, 100, 50, 10), # Starting at 50, L1000, returns to 50, password 10

        # Test sample input
        (50, 'L', 68, 100, 82, 1),
        (82, 'L', 30, 100, 52, 0),
        (52, 'R', 48, 100, 0, 1),
        (0, 'L', 5, 100, 95, 0),
        (95, 'R', 60, 100, 55, 1),
        (55, 'L', 55, 100, 0, 1),
        (0, 'L', 1, 100, 99, 0),
        (99, 'L', 99, 100, 0, 1),
        (0, 'R', 14, 100, 14, 0),
        (14, 'L', 82, 100, 32, 1),

        # Test regression bugs
        (0, 'R', 1, 100, 1, 0),
        (0, 'L', 1, 100, 99, 0),
        (0, 'L', 100, 100, 0, 1),
        (0, 'L', 101, 100, 99, 1),
        (99, 'R', 1, 100, 0, 1),
        (42, 'L', 100, 100, 42, 1),
        (42, 'L', 42, 100, 0, 1),
        (42, 'R', 100, 100, 42, 1),
        (42, 'R', 58, 100, 0, 1),
    ],
)
def test_rotate_dial(current_dial, direction, rotations, max_pos, expected, zero_dial_counts):
    """Tests the rotate_dial function with various valid inputs."""
    assert rotate_dial(current_dial, direction, rotations, max_pos) == (expected, zero_dial_counts)

def test_rotate_dial_invalid_direction():
    """Tests that rotate_dial raises a ValueError for an invalid direction."""
    with pytest.raises(ValueError, match="Invalid direction"):
        rotate_dial(5, "X", 10, MAX_POSITIONS)

def test_main_output(capsys):
    """Tests the output of the main function."""
    assert main(start_dial=50, input_file='test_input.csv') == (32, 6)
