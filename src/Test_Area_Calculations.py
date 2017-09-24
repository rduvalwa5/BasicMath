'''
Created on Sep 2, 2017

@author: rduvalwa2
'''
import unittest
import AreaCalculation

class test_AreaCalcualtions(unittest.TestCase):
    def setUp(self):
        print("Set up")
                    
    def test_SquareArea(self):
        area = AreaCalculation.math_areaCaluculations()
        num = 4
        expected = 16
        result = area.areaSquare(num)
        self.assertEqual(expected,result)
 
    def test_rectangleArea(self):
        area = AreaCalculation.math_areaCaluculations()
        sideH = 5
        sideW = 9
        expected = 45
        result = area.areaRectangle(sideH,sideW)
        self.assertEqual(expected,result)
        
    def test_CircleArea(self):
        area = AreaCalculation.math_areaCaluculations()
        radius = 5
        expected = 78.53975
        result = area.areaCirclcle(radius)
        self.assertEqual(expected,result)
        
    def test_ParallelgramArea(self):
        area = AreaCalculation.math_areaCaluculations()
        base = 4
        height = 6
        expected = 24
        result = area.areaParallelGram(base, height)
        self.assertEqual(expected,result)

    def test_TrapezoidArea(self):
        area = AreaCalculation.math_areaCaluculations()
        base1 = 4
        base2 = 6
        height = 8
        expected = 40
        result = area.areaTrapezoid(height,base1,base2)
#        result = height/2 * (base1 + base2)
        print("Result ", result)
        self.assertEqual(expected,result)  
        
    def test_elipseArea(self):
        area = AreaCalculation.math_areaCaluculations()
        r1 = 4
        r2 = 6
        expected = 75.39815999999999
        result = area.areaElipse(r1, r2)
        self.assertEqual(expected,result)   
        
    def test_equilateral_triangle(self): 
        area = AreaCalculation.math_areaCaluculations()
        side = 7
        expected =  (21.217622392718745+0j)
        result = area.equilateralTriangleArea(side)
        self.assertEqual(expected,result) 
        
    def tearDown(self):
        print("Tear Down")
                        
if __name__ == "__main__":
    unittest.main()        