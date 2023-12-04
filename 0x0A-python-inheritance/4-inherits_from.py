#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
