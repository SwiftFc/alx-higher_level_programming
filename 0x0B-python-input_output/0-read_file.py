#!/usr/bin/python3
"""A module to read a file and print to stdout"""


def read_file(filename=""):
    """Defines a function to read a file"""
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end='')
