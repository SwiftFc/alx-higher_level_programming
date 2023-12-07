#!/usr/bin/python3
"""A module to append text to a file"""


def append_write(filename="", text=""):
    """Defines a function to append text to the end of a file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
