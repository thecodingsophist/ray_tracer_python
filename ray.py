from vec3 import Vector

class Ray():
    #initialize ray
    def __init__(self, a = None, b = None):
        #e is a tuple
        self.A = a
        self.B = b

    def origin(self):
        return self.A

    def direction(self):
        return self.B

    def point_at_parameter(self, t):
        return self.A + t*self.B

    
