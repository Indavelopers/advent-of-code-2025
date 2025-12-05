# Day N
# 1/2 challenge
# Unit tests in test_solution1.py
# Run with: "python solution1.py test_input1.txt --debug | tee test_output1.txt"
# Final output: "python solution1.py input.txt | tee output1.txt"

import argparse
import logging


def load_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

        data = [d.strip() for d in data.split('\n')]

    return data


def process_item(item):
    """Process each item

    Process each battery bank and finds the largest joltage possible.
    Joltage is calculated as this: if for bank '12345' you turn on batteries '2' and '4', it outputs '24'.

    Args:
        item - str: Battery bank, as a str composed of 2+ digits, eg. '987654321111111'.

    Returns:
        Largest joltage possible, eg. '98' for the previous example.
    """

    logging.debug(f'process_item with arg: {item}')

    # Find the highest digit
    # Except if it's the last one, then the 2nd hightest
    # Then find the highest digit to the right of the first one

    max_digit = max(item)
    max_digit_index = item.index(max_digit)
    
    if max_digit_index == len(item) - 1:
        max_digit = max(item[:-1])
        max_digit_index = item.index(max_digit)

    logging.debug(f'Max digit: {max_digit}, index: {max_digit_index}')

    item_right_of_max_digit = item[max_digit_index + 1:]
    logging.debug(f'Item right of max digit: {item_right_of_max_digit}')

    second_max_digit = max(item_right_of_max_digit)
    second_max_digit_index = max_digit_index + item_right_of_max_digit.index(second_max_digit) + 1

    logging.debug(f'2nd Max digit: {second_max_digit}, index: {second_max_digit_index}')

    res = max_digit + second_max_digit

    return res


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
        
        res = process_item(r)
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
