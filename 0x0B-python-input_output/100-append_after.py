#!/usr/bin/python3

"""Input/Output Module"""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string if search_string is found"""

    text = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
