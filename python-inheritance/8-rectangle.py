#!/usr/bin/python3
""" Do inheritance """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        integer_validator("width", width)
        self.width = width
        integer_validator("width", height)
        self.height = height
