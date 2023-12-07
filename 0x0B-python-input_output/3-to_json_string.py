#!/usr/bin/python3
"""A module to convert to json"""
import json


def to_json_string(my_obj):
    """Returns a sjson representation of string obj"""
    data = json.dumps(my_obj)
    return data
