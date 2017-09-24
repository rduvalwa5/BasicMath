'''
Created on Sep 18, 2017
Trigonometric functions
https://docs.python.org/3.6/library/math.html
https://en.wikipedia.org/wiki/Trigonometric_functions

Basis of trigonometry: if two right triangles have equal acute angles, they are similar, so their side lengths are proportional. 
Proportionality constants are written within the image: sin θ, cos θ, tan θ, where θ is the common measure of five acute angles.
In mathematics, the trigonometric functions (also called circular functions, angle functions or goniometric functions[1][2]) are
functions of an angle. They relate the angles of a triangle to the lengths of its sides. Trigonometric functions are important in
the study of triangles and modeling periodic phenomena, among many other applications.
The most familiar trigonometric functions are the sine, cosine, and tangent. In the context of the standard unit circle 
(a circle with radius 1 unit), where a triangle is formed by a ray starting at the origin and making some angle with the x-axis, 
the sine of the angle gives the length of the y-component (the opposite to the angle or the rise) of the triangle, the cosine gives
the length of the x-component (the adjacent of the angle or the run), and the tangent function gives the slope (y-component divided 
by the x-component). More precise definitions are detailed below. Trigonometric functions are commonly defined as ratios of two sides
of a right triangle containing the angle, and can equivalently be defined as the lengths of various line segments from a unit circle. 
More modern definitions express them as infinite series or as solutions of certain differential equations, allowing their extension to 
arbitrary positive and negative values and even to complex numbers.

Trigonometric functions have a wide range of uses including computing unknown lengths and angles in triangles (often right triangles). 
In this use, trigonometric functions are used, for instance, in navigation, engineering, and physics. A common use in elementary physics 
is resolving a vector into Cartesian coordinates. The sine and cosine functions are also commonly used to model periodic function phenomena
such as sound and light waves, the position and velocity of harmonic oscillators, sunlight intensity and day length, and average temperature
variations through the year.

In modern usage, there are six basic trigonometric functions, tabulated here with equations that relate them to one another. 
Especially with the last four, these relations are often taken as the definitions of those functions, but one can define them equally 
well geometrically, or by other means, and then derive these relations.

https://www.mathsisfun.com/algebra/trig-finding-side-right-triangle.html
http://www.montereyinstitute.org/courses/DevelopmentalMath/COURSE_TEXT2_RESOURCE/U07_L1_T4_text_final.html
'''

import math
from _ast import Num

class Trig_Functions():
    '''
    Sine: sin(θ) = Opposite / Hypotenuse
    cos 60° = Adjacent / Hypotenuse 
    tan 53° = Opposite/Adjacent 
    
    Sine Θ = oposite/hypotenuse
    Cosine Θ = adjacent/hypotenuse
    Tangent Θ = oposite/adjacent
        
    "Opposite" is opposite to the angle θ
    "Adjacent" is adjacent (next to) to the angle θ
    "Hypotenuse" is the long one.
    
    '''
    def __init__(self):
#        self.theInput = num
#        print("Input is ", self.theInput)
        pass
    def get_Hypotenuse(self,adjacent,opposit):
        '''
        hypotenuse = square root of adjacent squared + opposite square
        '''
        return math.sqrt((adjacent * adjacent) + (opposit * opposit))
        
    '''
    The Pythagorean Theorem
    If a and b are the lengths of the legs of a right triangle and c is the length of the hypotenuse, 
    then the sum of the squares of the lengths of the legs is equal to the square of the length of the hypotenuse.
     This relationship is represented by the formula: 
     (adjacent * adjacent) + (opposit * opposit) = (hypotenuse * hypotenuse) 
    '''
    def get_adjacent_right_triangle(self,hypotenuse,opposit):
        '''
        (hypotenuse * hypotenuse) - (opposit * opposit)  = (adjacent * adjacent)
        '''
        return math.sqrt((hypotenuse * hypotenuse) - (opposit * opposit) )
        
    def get_opposit_right_triangle(self,hypotenuse,adjacent):
        '''
         (hypotenuse * hypotenuse) - (adjacent * adjacent) = (opposit * opposit)
        '''
        return math.sqrt((hypotenuse * hypotenuse) - (adjacent * adjacent))

    def get_angle(self):
        '''
        
        '''
        pass    
    
    def get_cosine(self,flt):
        '''
        parts of triangle  adjacent, opposit, hypotenuse
        math.acos(x)
        adjacent/hypotenuse
        Return the arc cosine of x, in radians.
        The cosine (sine complement, Latin: cosinus, sinus complementi) of an angle is the ratio of the length of the adjacent side to the length of the hypotenuse, so called 
        because it is the sine of the complementary or co-angle, the other non-right angle.[4] Because the angle sum of a triangle is π radians, 
        the co-angle B is equal to π/2 − A; so cos A = sin B = sin(π/2 − A). 
        In our case: cosA = adjacent / hypotenuse
        '''
#      print("Cosine for ",num ," is ", math.acos(self.theInput))
        return math.acos(flt)
    
    
if __name__ == '__main__':
    
    n = .888
    print(math.acos(.7))
    a = Trig_Functions()
    print(a.get_cosine(n))
    
    adjacent = 4
    opposit = 6
    x = Trig_Functions()
    hypotenuse = x.get_Hypotenuse(adjacent, opposit)
    print("hypotenuse is ", x.get_Hypotenuse(adjacent, opposit))
    print("adjacent is ", x.get_adjacent_right_triangle(hypotenuse, opposit))
    print("opposit is ", x.get_opposit_right_triangle(hypotenuse, adjacent))