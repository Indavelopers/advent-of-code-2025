# Day N
# 2/2 challenge
# Unit tests in test_solution2.py
# Run with: "python solution2.py test_input2.txt --debug | tee test_output2.txt"
# Final output: "time python solution2.py input.txt | tee output2.txt"

import argparse
import logging
from itertools import combinations


def load_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

        data = [d.strip() for d in data.split('\n')]

    return data


def process_item_gemini(item):
    """Process each item

    Process each battery bank and finds the largest joltage possible.
    Joltage is calculated as this: for a 15-digit bank, you enable 12 batteries so it reads the highest possible number
    Eg. for '987654321111111', it outputs '987654321111'

    Args:
        item - str: Battery bank, as a str composed of 15 digits, eg. '987654321111111'.

    Returns:
        int - Largest joltage possible, composed of 12 digits, eg. '987654321111' for the previous example.
    """

    logging.debug(f'process_item with arg: {item}')

    # Find the largest subsequence of 12 digits
    # Using a monotonic stack approach to find the lexicographically largest subsequence
    # This is O(N) where N is the length of the item, suitable for N=100.
    target_length = 12
    to_remove = len(item) - target_length
    stack = []

    for digit in item:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return int("".join(stack[:target_length]))


def process_item(item):
    """Process each item

    Process each battery bank and finds the largest joltage possible.
    Joltage is calculated as this: for a 15-digit bank, you enable 12 batteries so it reads the highest possible number
    Eg. for '987654321111111', it outputs '987654321111'

    Args:
        item - str: Battery bank, as a str composed of 15 digits, eg. '987654321111111'.

    Returns:
        int - Largest joltage possible, composed of 12 digits, eg. '987654321111' for the previous example.
    """

    logging.debug(f'process_item with arg: {item}')

    # Find the set of unique combinations of 12 digits from the 15 didgit item
    # Find the max integer out of the combinations
    
    item_combinations = set(combinations(item, 12))

    str_combinations = [''.join(c) for c in item_combinations]
    sorted_combinations = sorted(str_combinations)
    int_combinations = [int(c) for c in sorted_combinations]

    max_combination = max(int_combinations)

    return max_combination


def main(input_file_path, debug=False):
    logging.basicConfig(filename=str(input_file_path).replace('.txt', '.log'),
                        encoding='utf-8',
                        filemode='w',
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S %z',
                        level=logging.DEBUG if debug else logging.INFO)
    
    data = load_input(input_file_path)

    logging.debug('Loaded data:')
    logging.debug(data)

    results = 0
    for r in data:
        logging.debug(f'Processing: {r}')
        
        res = process_item_gemini(r)

        logging.debug(f'Result: {res}')
        
        results += int(res)

    logging.info(f'Results: {results}')

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process the input file for today's challenge.")
    parser.add_argument('input_file', type=str, help='Path to the input file (default., "input.txt").', default='input.txt')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')
    args = parser.parse_args()

    res = main(args.input_file, args.debug)
    print(res)
