from __future__ import division
import math

class Vector():
#initialize vector with vector data tuple 'e' with 3 items, otherwise, the default vector_data is None
    def __init__(self, e0 = None, e1 = None, e2 = None ):
        #e is a tuple
        self.e = (e0, e1, e2)
        #define variables that will be used throughout
        self.x = self.e[0]
        self.y = self.e[1]
        self.z = self.e[2]
        self.r = self.e[0]
        self.g = self.e[1]
        self.b = self.e[2]

    def print_properties_no_space(self):
        info = "%d%d%d" %(self.e[0], self.e[1], self.e[2])
        return info

    def print_properties_space(self):
        info = "%d %d %d" %(self.e[0], self.e[1], self.e[2])
        return info

    def length(self):
        return math.sqrt((e[0]*e[0] + e[1]*e[1] + e[2]*e[2]))

    def squared_length(self):
        return e[0]*e[0] + e[1]*e[1] + e[2]*e[2]

    def make_unit_vector(self):
        k = 1/self.length()
        self.e[0] *= k
        self.e[1] *= k
        self.e[2] *= k

    def add_by_vector(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self

    def multiply_by_vector(self, v):
        self.e[0] *= v.e[0]
        self.e[1] *= v.e[1]
        self.e[2] *= v.e[2]
        return self

    def divide_by_vector(self, v):
        self.e[0] /= v.e[0]
        self.e[1] /= v.e[1]
        self.e[2] /= v.e[2]
        return self

    def subtract_by_vector(self, v):
        self.e[0] -= v.e[0]
        self.e[1] -= v.e[1]
        self.e[2] -= v.e[2]
        return self

    def multiply_by_float(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def divide_by_float(self, t):
        k = 1.0/t
        self.e[0] *= k
        self.e[1] *= k
        self.e[2] *= k
        return self
