from __future__ import division
from ray import Ray
from vec3 import Vector
from vector_program import Vector_Functions
import math

# not sure if we need to initialize the background..
# def __init__(self):

def color(ray):
    unit_direction = Vector(ray.direction().make_unit_vector())
    t = 0.5(unit_direction.y() + 1.0)
    vector_A = Vector(1.0, 1.0, 1.0)
    vector_B = Vector(0.5, 0.7, 1.0)
    return (1.0 - t)*vector_A + t*vector_B

def main():

    f = open("color_bg.ppm", "w+")

    nx = 200
    ny = 100

    f.write("P3\n%d   %d   \n255\n" %(nx, ny))

    lower_left_corner = Vector(-2.0, -1.0, -1.0)
    horizontal = Vector(4.0, 0.0, 0.0)
    vertical = Vector(0.0, 2.0, 0.0)
    origin = Vector(0.0, 0.0, 0.0)

    for j in range(ny-1, 0, -1):
        for i in range(nx):
            u = i/nx
            v = j/ny
            horizontal = horizontal.multiply_by_float(u)
            vertical = vertical.multiply_by_float(v)
            sum_of_horizontal_and_vertical = add_two_vectors(horizontal, vertical)
            r = Ray(origin, add_two_vectors(lower_left_corner, sum_of_horizontal_and_vertical))
            col = Vector(color(r))
            ir = int(255.99*col[0])
            ig = int(255.99*col[1])
            ib = int(255.99*col[2])

            f.write("%d %d %d\n" %(ir, ig, ib))

    f.close()

if __name__ == "__main__":
    main()
