#!/usr/bin/python3
import magic_calculation_102

from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
    else:
        c = sub(a, b)

    for i in range(4, 6):
        c = add(c, i)

    return c
