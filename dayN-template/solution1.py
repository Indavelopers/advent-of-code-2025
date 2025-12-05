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

    return data


def fun1(arg):
    """One-line description

    Full description

    Args:
        arg: Arg description.

    Returns:
        Return description.
    """

    logging.debug(f'fun1 called with arg: {arg}')

    return arg


def main(input_file_path, debug=False):
    logging.basicConfig(filename=str(input_file_path).replace('.txt', '.log'),
                        encoding='utf-8',
                        filemode='w',
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S %z',
                        level=logging.DEBUG if debug else logging.INFO)
    
    data = load_input(input_file_path)

    logging.info('Loaded data:')
    logging.info(data)

    results = fun1(data)

    logging.info(f'Results: {results}')

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process the input file for today's challenge.")
    parser.add_argument('input_file', type=str, help='Path to the input file (default., "input.txt").', default='input.txt')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')
    args = parser.parse_args()

    res = main(args.input_file, args.debug)
    print(res)
