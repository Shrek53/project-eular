#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_3 = int((n - 1) / 3)
    max_5 = int((n - 1) / 5)
    max_15 = int((n - 1) / 15)

    n_3 = (3 * max_3 * (max_3 + 1)) >> 1
    n_5 = (5 * max_5 * (max_5 + 1)) >> 1
    n_15 = (15 * max_15 * (max_15 + 1)) >> 1

    summ = n_3 + n_5 - n_15
    print(summ)