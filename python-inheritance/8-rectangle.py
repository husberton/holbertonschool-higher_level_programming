#!/usr/bin/python3
""" Do inheritance """


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if integer_validator(width):
            self.width = width
        if integer_validator(height):
            self.height = height
