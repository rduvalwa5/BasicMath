'''
Created on Sep 4, 2017
Created for Jenkins Example
https://docs.python.org/3.6/library/math.html
https://docs.python.org/3/library/math.html
http://math2.org/math/geometry/areasvols.htm
math precedence  https://www.math.utah.edu/online/1010/precedence/
http://www.math.com/tables/geometry/volumes.htm
https://docs.python.org/3/library/math.html
@author: rduvalwa2
'''
import math

class math_volumeCaluculations():   
    def pi(self):
        return 3.141592653589793
    
    def powers(self,val,raiseTo):
        return  pow(val,raiseTo)
    
    def cube_volume(self,side):
        return pow(side, 3)

    def rectangular_prism_volume(self,a,b,c):
        return a*b*c
    
    def rightCylander_volume(self,height,radius):
        return math.pi * radius * 2 * height
    
    def pyramid_volume(self,length,width,height):
        return (length * width * height)/3

    def cone_volume(self,radius,height):
#        1/3 pi r 2 h
        return (math.pi * radius * height * 2)/3
    
    def sphere_volume(self, radius):
        return  (4/3) * math.pi * pow(radius,3)
    
    def ellipsoid_volume(self, radius1,radius2,radius3):
        return (4/3) * math.pi * radius1 * radius2 * radius3




if __name__ == '__main__':
    
    vol = math_volumeCaluculations()
    print(vol.pi())
    print(vol.cube_volume(4))
    print(vol.rectangular_prism_volume(3, 4, 5))
    print(vol.rightCylander_volume(10, 5))
    print(vol.pyramid_volume(6, 5, 4))
    print(vol.cone_volume(6, 5))
    print(vol.sphere_volume(5));
    print(vol.ellipsoid_volume(6,4, 5))