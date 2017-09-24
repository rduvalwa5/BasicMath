'''
Created on Sep 13, 2017
https://docs.python.org/3.6/library/math.html
Power and logarithmic functions
@author: rduvalwa2
'''

import unittest
import math
import cmath

class test_PowersAndLogFunctions(unittest.TestCase):
    def test_exp(self):
        '''
        Return e**x.
        Return e**x - 1. For small floats x, the subtraction in exp(x) - 1 can result in a significant loss of precision; 
        the expm1() function provides a way to compute this quantity to full precision:
        '''
        expected = 403.4287934927351
        num = 6
        result = math.exp(num)
        self.assertEqual(expected, result,"expected 403.4287934927351")
        
    def test_expm1(self):
        '''
        math.expm1(x)
        Return e**x - 1. For small floats x, the subtraction in exp(x) - 1 
        can result in a significant loss of precision; the expm1() function provides a way to compute 
        this quantity to full precision:
        '''
        num = 6
        expected = 402.4287934927351
        result = math.expm1(num)
        self.assertEqual(expected, result,"expected 403.4287934927351")
        
    def test_log(self):
        '''
        math.log(x[, base])
        With one argument, return the natural logarithm of x (to base e).
        With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
        '''
        num = 6
        expected = 1.791759469228055
        result = math.log(num)
        self.assertEqual(expected, result,"expected 1.791759469228055")
        result = math.log(num,10)
        expected = 0.7781512503836435
        self.assertEqual(expected, result,"expected 0.7781512503836435")
        result = math.log(num,2)
        expected = 2.584962500721156
        self.assertEqual(expected, result,"expected 2.584962500721156")
        try:
            result = math.log(num,1)
        except Exception:
            self.assertRaises(ZeroDivisionError)
        
    def test_pow(self):
        '''
        math.pow(x, y)
        Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. 
        In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y 
        are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
        Unlike the built-in ** operator, math.pow() converts both its arguments to type float. Use ** or the built-in pow() function for computing exact integer powers.
        '''
        n = 5
        p = 6
        result = n
        i = 1
        while i < p + 1:
            if i == 1:
                print("power of ", i , n)
            else:
                result = result * n
                print("power of ", i , result)
            i = i + 1
        result = result * 1.0
        print("result is ", result)
        print("math.pow(5,6) ", math.pow(5,6))
        shortCut = (5 ** 6) * 1.0
        print("shortCut ", shortCut)
        self.assertEqual(result, math.pow(5,6), "pow test failed")
        self.assertEqual(shortCut, math.pow(5,6), "** test failed")
        
    def test_power_Error(self):
        '''
        If both x and y are finite, x is negative, and y is not an integer then pow(x, y) 
        is undefined, and raises ValueError.
        '''
        n = -5
        p = 6.66
        try:
            result = math.pow(n,p)
            print("Error result ", result)
        except Exception as e:
            print("Error for -5 and power of 6.66 is", e)
            self.assertRaises(ValueError)
 
    def test_powerOfZero(self):           
        n = -5
        p = 0
        expected = 1
        result = math.pow(n,p)
        print("No Error result for -5 and power of 0 is ", result)
        self.assertEqual(expected, result, "-5 to power of 0 expected is 1")

    def test_sqrt(self):
        '''
        math.sqrt(x)
        Return the square root of x.
        '''   
        expected = 3
        n = 9
        actual = math.sqrt(n)
        self.assertEqual(expected, actual, "sqare root failed")
        
        
if __name__ == "__main__":
    unittest.main()   