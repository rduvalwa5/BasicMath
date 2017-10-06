'''
Created on Sep 25, 2017
https://docs.python.org/3/library/math.html#trigonometric-functions
@author: rduvalwa2
'''

import math

class Trig_functions:
    def __init__(self,a,b):
        self.adjacent = a
        self.opposit = b
    
    def convert_radians_to_degrees(self,radian):
        '''
        9.2.4. Angular conversion
            math.degrees(x)
            Convert angle x from radians to degrees.
        '''
        return math.degrees(radian)
    
    def convert_degrees_to_radians(self,angle):
        '''
        9.2.4. Angular conversion
            math.radians(x)
            Convert angle x from degrees to radians.
        '''
        return math.radians(angle)
    
    def get_Cosine(self):
        '''
        co·sine
        the trigonometric function that is equal to the ratio of the side adjacent 
        to an acute angle (in a right-angled triangle) to the hypotenuse.
        adjacent/hypotenuse
        https://en.wikipedia.org/wiki/Trigonometric_functions
        '''
        cosine_radians = self.adjacent/self.get_hypotenuse()
        return  cosine_radians
    
    def get_Sine(self):
        '''
        sine(A) = opp/hyp = y/h
        sine
        the trigonometric function that is equal to the ratio of the side opposite a given angle 
        (in a right triangle) to the hypotenuse.
        '''
        sine_ratio = self.opposit/self.get_hypotenuse()
        return sine_ratio
    
    def get_sine_ratio_from_angle(self,angl):
        '''
        The method sin() returns the sine of x, in radians.
        '''
        return math.sin(angl)
 
    def get_cosine_ratio_from_angle(self,angl):
        '''
        '''
        return math.cos(angl)           
    
    def get_hypotenuse(self):
        '''
        Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin
        to point (x, y).
        '''
        return math.sqrt((self.adjacent * self.adjacent) + (self.opposit * self.opposit))
    
    def get_cos_angle_know_adj_opp(self):
        '''
        Pythagorean Theorem
        The formula that relates the lengths of the sides of any right triangle: 
        where c is the hypotenuse, and a and b are the legs of the right triangle.
        a squared + b squared = c squared
            >>> A = 7
            >>> B = 7
            >>> C = 9.899
            >>> from math import acos, degrees
            >>> degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
            89.99594878743945
        '''
        adj = self.adjacent
        opp = self.opposit
        hyp = math.sqrt((adj * adj) + (opp * opp))

        return math.degrees(math.acos((adj * adj + opp * opp - hyp * hyp)/(2.0 * adj * opp)))
 
    def get_sine_angle_know_adj_opp(self):
        '''
        Pythagorean Theorem
        The formula that relates the lengths of the sides of any right triangle: 
        where c is the hypotenuse, and a and b are the legs of the right triangle.
        a squared + b squared = c squared
            >>> A = 7
            >>> B = 7
            >>> C = 9.899
            >>> from math import acos, degrees
            >>> degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
            89.99594878743945
        '''
        adj = self.adjacent
        opp = self.opposit
        hyp = math.sqrt((adj * adj) + (opp * opp))

        return math.degrees(math.asin((adj * adj + opp * opp - hyp * hyp)/(2.0 * adj * opp)))       

    def get_angle_radians(self):
        angleList = []
        radianList = []
        angleRadianList = []
        for item in range(0,360):
            angleList.append(item)
        for angle in angleList:
            angleRadianList.append((angle,math.radians(angle)))

        return angleRadianList




if __name__ == '__main__':
    adj = 4.0
    opp = 3.0
    xx = Trig_functions(adj,opp)
    angleRadians = xx.get_angle_radians()
    for item in angleRadians:
        print(item)
        print(math.degrees(item[1]))
        
    
    '''
    adj = 4.0
    opp = 3.0
    xx = Trig_functions(adj,opp)
    print(xx.get_cos_angle_know_adj_opp())
    
    adj = 3.0
    opp = 4.0
    xx = Trig_functions(adj,opp)
    print(xx.get_sine_angle_know_adj_opp())
    ''' 