START_DIAL = 50
MAX_POSITIONS = 100


def rotate_dial(current_dial, direction, rotations, max_positions=MAX_POSITIONS):
    if direction == 'L':
        new_dial = (current_dial - rotations) % max_positions

        diff = current_dial - rotations
        # If diff is negative, you've crossed the 0 position
        if diff <= 0:
            # Current dial is an integer [0, 99]
            # If it was greater than 0, or thus not 0, there's a first revolution
            zero_dial_counts = 1 if current_dial != 0 else 0
        
            # Add more revolutions if diff >= max_positions
            zero_dial_counts += abs(diff) // max_positions
        else:
            zero_dial_counts = 0
    elif direction == 'R':
        new_dial = (current_dial + rotations) % max_positions
        zero_dial_counts = (current_dial + rotations) // max_positions
    else:
        raise ValueError('Invalid direction')
    
    return new_dial, zero_dial_counts

def main(start_dial, input_file):
    current_dial = start_dial

    print(f'Starting dial position: {current_dial}')

    password = 0
    movements = []
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            direction, rotations_str = line[0], line[1:]
            rotations = int(rotations_str)

            movements.append((direction, rotations))

    for i, (direction, rotations) in enumerate(movements):
        current_dial, zero_dial_counts = rotate_dial(current_dial, direction, rotations)

        password += zero_dial_counts

        print(f'Movement #{i+1}: dir {direction}, rotation {rotations}, dial {current_dial}, password {password}')

    print(f'Final dial position: {current_dial}, password: {password}')

    return current_dial, password


if __name__ == '__main__':
    main(start_dial=START_DIAL, input_file='input.csv')
