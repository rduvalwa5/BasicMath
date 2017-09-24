'''
Created on Sep 10, 2017

@author: rduvalwa2
'''
import unittest
from VolumeCalculation import math_volumeCaluculations
import math

class test_VolumeCalcualtions(unittest.TestCase):
    def setUp(self):
        print("Set up")
                    
    def test_Pi(self):
        inst = math_volumeCaluculations()
        pi = inst.pi()
        expected = math.pi
        self.assertEqual(expected,pi, "pi value fails")
        
    def test_powers(self):
        inst = math_volumeCaluculations()
        expected = 27
        self.assertEqual(expected,inst.powers(3, 3))
        
    def test_cubeVolume(self):
        inst = math_volumeCaluculations()
        expected = 64
        self.assertEqual(expected, inst.cube_volume(4) , "cube volume failed")
 
    def test_rectangular_prism_volume(self):
        inst = math_volumeCaluculations()
        expected = 4 * 5 * 6
        self.assertEqual(expected,inst.rectangular_prism_volume(4,5,6), "rectangular_prism_volume failed")       

    def test_rightCylander_volume(self):
        inst = math_volumeCaluculations()
        expected = math.pi * 5 * 6 * 2
        self.assertEqual(expected, inst.rightCylander_volume(5,6), "rightCylander_volumefailed")       

    def test_pyramid_volume(self):
        inst = math_volumeCaluculations()
        expected = (4 * 5 * 6)/3
        self.assertEqual(expected, inst.pyramid_volume(4,5,6), "pyramid volume failed")       
 
    def test_cone_volume(self):
        inst = math_volumeCaluculations()
        radius = 5
        height = 6
        expected = (math.pi * radius * height * 2)/3
        self.assertEqual(expected, inst.cone_volume(radius,height), "cone volume failed")       
   
    def test_sphere_volume(self):
        inst = math_volumeCaluculations()
        radius = 5
        expected = (4/3) * math.pi * pow(radius,3)
        self.assertEqual(expected,inst.sphere_volume(radius), "sphere volume failed")       

    def test_ellipsoid_volume(self):
        inst = math_volumeCaluculations()
        radius1 = 6
        radius2 = 4
        radius3 = 5
        expected = (4/3) * math.pi * radius1 * radius2 * radius3
        self.assertEqual(expected, inst.ellipsoid_volume(radius1,radius2,radius3), "ellipsoid volume failed")       
           
    def test_for_git(self):
        pass
    
    
     
    def tearDown(self):
        print("Tear Down")
                        
if __name__ == "__main__":
    unittest.main()             