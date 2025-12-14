#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits another class """
    def __init__(self, width, height):
        self.integer_validator(width)
        self.width = width
        self.integer_validator(height)
        self.height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
