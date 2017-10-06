'''
https://www.mathsisfun.com/algebra/trig-sine-law.html
https://en.wikipedia.org/wiki/Law_of_sines
'''
import math

class LawOfSinesRightAngle:
    '''
    In trigonometry, the law of sines, sine law, sine formula, or sine rule is an equation relating the lengths 
    of the sides of a triangle (any shape) to the sines of its angles. According to the law,
    a/sin A = b/sin B = c/sin C = d ,
    where a, b, and c are the lengths of the sides of a triangle, and A, B, and C are the opposite angles
    (see the figure to the right), while d is the diameter of the triangle's circumcircle. 
    When the last of these equations is not used, the law is sometimes stated using the reciprocals;
    sin A/a = sin B/b = sin C/c
    The law of sines can be used to compute the remaining sides of a triangle when two angles and a side are known—a 
    technique known as triangulation. Numerical calculation using this technique may result in a numerical error if 
    an angle is close to 90 degrees. It can also be used when two sides and one of the non-enclosed angles are known. 
    In some such cases, the triangle is not uniquely determined by this data (called the ambiguous case) and the technique 
    gives two possible values for the enclosed angle.
    
    Pythagorean Theorem
    The formula that relates the lengths of the sides of any right triangle: 
    where c is the hypotenuse, and a and b are the legs of the right triangle.
    a squared + b squared = c squared
    '''
    def __init__(self,a=0,b=0,c=0): #,angle_a=45,angle_b=90,angle_c=45):
        self.adjacent = a
        self.opposit = b
        self.hypotenuse = c
        self.adjacent_angle = 45
        self.opposit_angle = 45
        self.angle = 90
        
    
    def get_angle_opposit(self):
        pass
    
    def get_angle_adjacent(self):
        pass
    
    def get_adjacent_side(self):
#        self.hypotenuse = h
        print(self.hypotenuse, self.opposit)
        return math.sqrt(self.hypotenuse**2 - self.opposit**2)
    
    def get_hypotenuse(self,adjacent,opposit):
        self.adjacent = adjacent
        self.opposit = opposit
        return math.sqrt(self.adjacent**2 + self.opposit**2)
    
class lawOfCosine():
    '''
    c squared = a squared + b squared - 2abcosC
    C is the angle
    The law of cosines for calculating one side of a triangle when the angle opposite and 
    the other two sides are known. Can be used in conjunction with the law of sines to find 
    all sides and angles. 
    '''
    def __init__(self):
        pass
    
    def get_angle(self,a,b,c):
        return a**2 + b**2 - c**2
    
if __name__ == '__main__':

        lg = LawOfSinesRightAngle(0,3,5)
        adjacentSide = lg.get_adjacent_side()
        print("adjacent side is ", adjacentSide)
        
        cg = lawOfCosine()
        print(cg.get_angle(5, 4, 3))