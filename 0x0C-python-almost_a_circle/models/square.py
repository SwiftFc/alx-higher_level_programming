#!/usr/bin/python3
"""Defines a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return (
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.size)
            )

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            for a, arg in enumerate(args):
                if a == 0 and arg is not None:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == 'id':
                    self.id = b
                elif a == 'size':
                    self.size = b
                elif a == 'x':
                    self.x = b
                elif a == 'y':
                    self.y = b

    def to_dictionary(self):
        """Converts the square object into dictionary format"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
