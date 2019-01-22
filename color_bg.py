from __future__ import division
from ray import Ray
from vec3 import Vector
from vector_program import *
import math

# not sure if we need to initialize the background..
# def __init__(self):

def color(ray):

    ray_direction_unit_vector = ray.direction().make_unit_vector()

    x = ray_direction_unit_vector.x
    y = ray_direction_unit_vector.y
    z = ray_direction_unit_vector.z

    unit_direction = Vector(x, y, z)
    y = unit_direction.get_y()
    t = 0.5*(y + 1.0)
    vector_A = Vector(1.0, 1.0, 1.0)
    vector_B = Vector(0.5, 0.7, 1.0)

    return add_two_vectors(vector_A.multiply_by_float(1.0 - t), vector_B.multiply_by_float(t))

def main():

    f = open("color_bg.ppm", "w+")

    nx = 200
    ny = 100

    f.write("P3\n%d   %d   \n255\n" %(nx, ny))

    lower_left_corner = Vector(-2.0, -1.0, -1.0)
    horizontal = Vector(4.0, 0.0, 0.0)
    vertical = Vector(0.0, 2.0, 0.0)
    origin = Vector(0.0, 0.0, 0.0)

    # for j in range(nx):
    #     for i in range(ny-1, 0, -1):
    for j in range(ny-1, 0, -1):
        for i in range(nx):
            u = i/nx
            #print("u: " + str(u))
            v = j/ny
            #print("v: " + str(v))

            #calculates the direction of the ray
            horizontal = horizontal.multiply_by_float(u)
            vertical = vertical.multiply_by_float(v)
            sum_of_horizontal_and_vertical = add_two_vectors(horizontal, vertical)
            direction = add_two_vectors(lower_left_corner, sum_of_horizontal_and_vertical)

            r = Ray(origin, direction)
            col = color(r)
            # ir = int(255.99*col.r)
            # ig = int(255.99*col.g)
            # ib = int(255.99*col.b)

            ir = 255.99*col.r
            ig = 255.99*col.g
            ib = 255.99*col.b

            f.write("%d %d %d\n" %(ir, ig, ib))

    f.close()

if __name__ == "__main__":
    main()
