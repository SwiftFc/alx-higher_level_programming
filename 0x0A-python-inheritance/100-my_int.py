#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return int(self) != int(value)

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return int(self) == int(value)
