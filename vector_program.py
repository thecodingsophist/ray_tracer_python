from vec3 import Vector

#class Vector_Functions():
#NOTE TO SELF: this does not need to be a class, if is class then initialize it when using it

def add_two_vectors(vector_1, vector_2):

    #make the e vector using the sum of each vector component from vector_1 and vector_2
    vector_3_e0 = vector_1.e[0] + vector_2.e[0]
    vector_3_e1 = vector_1.e[1] + vector_2.e[1]
    vector_3_e2 = vector_1.e[2] + vector_2.e[2]

    vector_3 = Vector(vector_3_e0, vector_3_e1, vector_3_e2)
    return vector_3

def subtract_vectors(vector_1, vector_2):

    #make the e vector using the difference of each vector component from vector_1 and vector_2
    vector_3_e0 = vector_1.e[0] - vector_2.e[0]
    vector_3_e1 = vector_1.e[1] - vector_2.e[1]
    vector_3_e2 = vector_1.e[2] - vector_2.e[2]

    vector_3 = Vector(vector_3_e0, vector_3_e1, vector_3_e2)
    return vector_3

def multiply_vectors(vector_1, vector_2):

    vector_3_e0 = vector_1.e[0] * vector_2.e[0]
    vector_3_e1 = vector_1.e[1] * vector_2.e[1]
    vector_3_e2 = vector_1.e[2] * vector_2.e[2]

    vector_3 = Vector(vector_3_e0, vector_3_e1, vector_3_e2)
    return vector_3

def divide_vectors(vector_1, vector_2):

    vector_3_e0 = vector_1.e[0] / vector_2.e[0]
    vector_3_e1 = vector_1.e[1] / vector_2.e[1]
    vector_3_e2 = vector_1.e[2] / vector_2.e[2]

    vector_3 = Vector(vector_3_e0, vector_3_e1, vector_3_e2)
    return vector_3

def multiply_vectors_by_constant(constant, vector_1):

    vector_2_e0 = constant * vector_1.e[0]
    vector_2_e1 = constant * vector_1.e[1]
    vector_2_e2 = constant * vector_1.e[2]

    vector_2 = Vector(vector_2_e0, vector_2_e1, vector_2_e2)
    return vector_2

def multiply_by_float(float, vector_1):

    vector_2_e0 = float * vector_1.e[0]
    vector_2_e1 = float * vector_1.e[1]
    vector_2_e2 = float * vector_1.e[2]

    vector_2 = Vector(vector_2_e0, vector_2_e1, vector_2_e2)
    return vector_2

#THIS METHOD ALREADY EXISTS IN VEC3
# def divide_vectors_by_constant(constant, vector_1):
#
#     vector_2_e0 = vector_1.e[0] / constant
#     vector_2_e1 = vector_1.e[1] / constant
#     vector_2_e2 = vector_1.e[2] / constant
#
#     vector_2 = Vector(vector_2_e0, vector_2_e1, vector_2_e2)
#     return vector_2

def dot_product(vector_1, vector_2):
    return vector_1.e[0] * vector_2.e[0] + vector_1.e[1] * vector_2.e[1] + vector_1.e[2] * vector_2.e[2]

# def cross_product(vector_1, vector_2):
#     return vector_3 = Vector( (vector_1.e[1]*vector_2.e[2] - vector_1.e[2]*vector_2.e[1]), (-(vector_1.e[0]*vector_2.e[2] - vector_1.e[2]*vector_2.e[0])), (vector_1.e[0]*vector_2.e[1] - vector_1.e[1]*vector_2.e[0]))
