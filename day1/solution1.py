START_DIAL = 50
MAX_POSITIONS = 100


def rotate_dial(current_dial, direction, rotations, max_positions=MAX_POSITIONS):
    if direction == 'L':
        current_dial = (current_dial - rotations) % max_positions
    elif direction == 'R':
        current_dial = (current_dial + rotations) % max_positions
    else:
        raise ValueError('Invalid direction')
    
    return current_dial

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
        current_dial = rotate_dial(current_dial, direction, rotations)

        print(f'Movement #{i+1}: dir {direction}, rotation {rotations}, dial {current_dial}')

        if current_dial == 0:
            password += 1

    print(f'Final dial position: {current_dial}, password: {password}')

    return current_dial, password


if __name__ == '__main__':
    main(start_dial=START_DIAL, input_file='input.csv')
