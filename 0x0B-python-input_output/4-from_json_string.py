#!/usr/bin/python3
"""A module to convert json to a python object"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    data = json.loads(my_str)
    return data
