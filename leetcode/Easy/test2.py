#!/bin/python

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.breadth * self.length


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius


rec = Rectangle(12, 10)
print(rec.area())