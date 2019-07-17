#!/usr/bin/python

'''
Question at hand?
    Given a list of stock prices at various times,
    calculate the most money that can be made.
    Ideally, find the lowest price for the buy
    and the highest price to sell.
    However, there are stipulations and limitations.

Limitations
    For every list of data, you must first buy a stock
    before you can sell it.
    So just finding the max and min of the data set
    and taking the diff ain't gunna cut it.

Edge Cases
    Some interesting things arise here because of that restriction
    and the arrangement of the data points chronologically.
    What do you do if the list of prices is empty?
    What do you do if it only has one element?
    These are edge cases that need clarification,
    as they are not addressed in the problem description.

    arr[int] input
    find max value
    find min value - should be consant
    if position of max value is after min value then subtract min from max value
    if position of max value is before min then
        find next max value
        compare position of current max value with min
        if position of max value is after min value then subtract min from max
        if position of max value is before min then
            find next max value ... see a pattern?
    int output
'''

import argparse


def find_max_profit(prices):
    if len(prices) < 2:
        return 'Please supply a list with at least 2 prices.'

    min_val = prices[0]
    max_profit = prices[1] - prices[0]

    for curr_t in range(1, len(prices)):
        curr_val = prices[curr_t]
        curr_profit = curr_val - min_val
        max_profit = max(max_profit, curr_profit)
        min_val = min(min_val, curr_val)
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.'
    )
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='an integer price'
    )
    args = parser.parse_args()
    profit = find_max_profit(args.integers)
    prices = args.integers
    print(f'A profit of ${profit} can be made from the stock prices {prices}.')
