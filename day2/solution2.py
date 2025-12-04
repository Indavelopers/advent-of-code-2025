# Day 2
# 1/2 challenge

import argparse
import logging
from typing import List

from more_itertools import sliced

logger = logging.getLogger(__name__)


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

        logger.debug(f'Checking ID: {id_str}')
        
        len_id = len(id_str)

        for slice_length in range(1, len_id // 2 + 1):
            try:
                slices = list(sliced(id_str, slice_length, strict=True))

                logger.debug(f'Slices of length {slice_length}: {slices}')

                first_slice = slices[0]
                all_slices_are_equal = all(first_slice == s for s in slices)

                logger.debug(f'All slices are equal: {all_slices_are_equal}')

                if all_slices_are_equal:
                    invalid_ids.append(id)

                    break   # As soon as we find a repeating slice, we don't check other slices and continue with the next ID
            except ValueError: # Sliced with strict mode raises ValueError if can't slice sequence in equal-length slices
                continue

    return invalid_ids


def main(input_file_path, debug=False):
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    
    id_ranges = load_input(input_file_path)

    logger.debug('Loaded ranges:')
    logger.debug(id_ranges)

    all_invalid_ids = []
    for id_range in id_ranges:
        logger.debug(f'ID range: {id_range}')

        invalid_ids = find_invalid_ids(id_range)

        logger.debug(f'Invalid IDs: {invalid_ids}')

        all_invalid_ids += [id for id in invalid_ids]

    logger.debug('All invalid IDs:')
    logger.debug(all_invalid_ids)

    sum_all_invalid_ids = sum(all_invalid_ids)
    logger.debug(f'Sum of invalid IDs: {sum_all_invalid_ids}')

    print(sum_all_invalid_ids)

    return sum_all_invalid_ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process the input file for Day 2's challenge.")
    parser.add_argument('input_file', type=str, help='Path to the input file (e.g., input.txt).')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')
    args = parser.parse_args()

    main(args.input_file, args.debug)
