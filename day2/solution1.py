# Day 2
# 1/2 challenge

import argparse
import pprint
from typing import List


def load_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    data = content.split(',')
    data = [s.strip() for s in data]

    return data


def find_invalid_ids(id_range_str: str) -> List[str]:
    """Finds invalid IDs within a given numerical range.

    This function parses a string that defines a numerical range. It then
    identifies and collects all numbers within that range that are considered
    "invalid" according to specific criteria.

    Args:
        range_str: A string composed of two numbers separated by a hyphen,
            representing the start and end of the range (e.g., "100-200").

    Returns:
        A list of strings, where each element is an invalid ID found within
        the specified range. The list will be empty if no invalid IDs are
        found.
    """
    invalid_ids = []

    start_id_str = id_range_str.split('-')[0]
    end_id_str = id_range_str.split('-')[1]

    start_id = int(start_id_str)
    end_id = int(end_id_str)

    id_range = range(start_id, end_id + 1)

    for id in id_range:
        id_str = str(id)

        print(f'Checking ID: {id_str}')

        if len(id_str) % 2 == 0:
            first_half = id_str[:len(id_str) // 2]
            second_half = id_str[len(id_str) // 2:]

            if first_half == second_half:
                print(f'Invalid ID: {id_str}')
                invalid_ids.append(id)
        else:
            print('ID has an odd number of digits')

    return invalid_ids


def main(input_file_path):
    id_ranges = load_input(input_file_path)

    print('Loaded ranges:')
    pprint.pp(id_ranges)
    print()

    all_invalid_ids = []
    for id_range in id_ranges:
        print(f'ID range: {id_range}')

        invalid_ids = find_invalid_ids(id_range)

        print(f'Invalid IDs: {invalid_ids}')
        print()

        all_invalid_ids += [id for id in invalid_ids]

    print('All invalid IDs:')
    pprint.pp(all_invalid_ids)
    print()

    sum_all_invalid_ids = sum(all_invalid_ids)
    print(f'Sum of invalid IDs: {sum_all_invalid_ids}')

    return sum_all_invalid_ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process the input file for Day 2's challenge.")
    parser.add_argument('input_file', type=str, help='Path to the input file (e.g., input.txt).')
    args = parser.parse_args()

    main(args.input_file)
