from __future__ import division
from vec3 import Vector
from vector_program import Vector_Functions

def main():
#open a file for writing and create if if it does not exist
    f = open("second_program_vectors.ppm", "w+")
#write some lines of pixel data to the file
    nx = 200;
    ny = 100;
    f.write("P3\n%d   %d   \n255\n" %(nx, ny))
    #to reverse count, go from high range to low range and add -1
    for j in range(ny-1, 0, -1):
        for i in range(nx):
            #calculates the pixels
            color = Vector(i/nx, j/ny, 0.2)
            ir = int(255.99*color.e[0])
            ig = int(255.99*color.e[1])
            ib = int(255.99*color.e[2])
            #writes in the file the rgb values of each pixel
            f.write("%d %d %d\n" %(ir, ig, ib))

#close the file when done
    f.close()

if __name__ == "__main__":
    main()
