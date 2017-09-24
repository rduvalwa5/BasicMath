'''
Created on Sep 2, 2017
Created for Jenkins Example
https://docs.python.org/3.6/library/math.html
https://docs.python.org/3/library/math.html
http://math2.org/math/geometry/areasvols.htm

math precedence  https://www.math.utah.edu/online/1010/precedence/
@author: rduvalwa2
'''
from cmath import sqrt

class math_areaCaluculations():
    
    def pi(self):
        return 3.14159

    def areaSquare(self,side):
        return side * side
    
    def areaRectangle(self,sideh,sidew):
        return sideh * sidew
    
    def areaCirclcle(self,radius): 
#        pi = 3.14159      
        return self.pi() * radius * radius
    
    def areaParallelGram(self,base,height):
        return  base * height 
    
    def areaTrapezoid(self,height,base1,base2):
        r1 = height/2
        r2 = base1 + base2
        r3 = r1 * r2
        print("R3 ",r3)
        return  (height/2)*(base1 + base2)
    
    def areaElipse(self,r1,r2):
        return self.pi()*r1*r2
    
    def areaTriangle(self,base,height):
        return (base * height)/2 
    
    def equilateralTriangleArea(self,side):
        '''
        https://www.google.com/search?q=calculate+area+of+equilateral+triangle&oq=calculate+area+of+equalateral+triangle&gs_l=psy-ab.1.0.0i13k1j0i13i5i30k1j0i8i13i10i30k1l2.2995.6728.0.11126.12.12.0.0.0.0.163.1251.6j6.12.0....0...1.1.64.psy-ab..0.12.1248...35i39k1j0i7i30k1j0i8i7i10i30k1j0i8i7i30k1j0i7i10i30k1.6EVC7GVUH70
        '''
        a = sqrt(3)
        x = (side * side) * a/4
        return x
    
if __name__ == '__main__':

        area = math_areaCaluculations()
        print(area.areaSquare(4))
        print(area.areaCirclcle(5))
        print(area.areaParallelGram(4, 6))
        print(area.areaTrapezoid(9,4, 6))
        print(area.areaElipse(4, 6))
        print(area.areaTriangle(4, 6))
        print(area.areaTriangle(4, 6))
        print(area.equilateralTriangleArea(7))