#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    current = [['rock'], ['paper'], ['scissors']]

    def recursion_helper(list):
        possibilities = [['rock'], ['paper'], ['scissors']]
        new_list = []
        for item in list:
            for possibility in possibilities:
                new_list.append(item + possibility)
        return new_list
    if n == 0:
        return [[]]
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]
    i = 1
    while i < n:
        current = recursion_helper(current)
        i += 1
    return current


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
