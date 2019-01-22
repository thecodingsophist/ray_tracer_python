from __future__ import division
from vec3 import Vector
from vector_program import *
import math

def main():
    A = Vector(1, 1, -1)
    float = 0.9999999

    B = multiply_by_float(float, A)
    print("B=" + str(B.get_r()))
    B.print_properties_space()

if __name__ == "__main__":
    main()
