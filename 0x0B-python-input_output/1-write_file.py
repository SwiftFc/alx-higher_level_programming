#!/usr/bin/python3
"""A module to write text into a file"""


def write_file(filename="", text=""):
    """Defines a function to write text into a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
