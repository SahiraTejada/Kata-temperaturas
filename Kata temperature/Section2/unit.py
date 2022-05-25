import sys
import unittest
from SectionSecond import *


class Instance_test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Instance_test, self).__init__(*args, **kwargs)
        self.attribute = Temperature
        self.scale = Scalename
    
    #Test To Celsius from F
    def test_ToCelsiusF(self):
        t = Temperature(32, Scalename.F)
        self.assertEqual(t.ToCelsius().Number, 0)
        pass
    #Test To Celsius from K
    def test_ToCelsiusK(self):
        t = Temperature(389, Scalename.K)
        self.assertEqual(t.ToCelsius().Number, 115.85)
        pass

    #Test To Farenheit from C
    def test_FarenheitC(self):
        t = Temperature(110, Scalename.C)
        self.assertEqual(t.ToFarenheit().Number, 230)
        pass
    
    #Test To Farenheit from K
    def test_FarenheitF(self):
        t = Temperature(285.37, Scalename.K)
        self.assertEqual(t.ToFarenheit().Number, 54)
        pass

    #Test To Kelvin from C
    def test_ToKevinC(self):
        t = Temperature(26.85, Scalename.C)
        self.assertEqual(t.ToKelvin().Number, 300)
        pass

    #Test To Kelvin from F
    def test_ToKevinK(self):
        t = Temperature(12, Scalename.F)
        self.assertEqual(t.ToKelvin().Number, 262.04)
        pass

    #Test To Add When the scale temperature is the same
    def test_ToAddEqual(self):
        t = Temperature(32, Scalename.F)
        tp = Temperature(32, Scalename.F)
        self.assertEqual(t.Add(tp).Number, 64)
        pass
    #Test To Add When the scale temperature is not  the same
    def test_ToAddNoEqual(self):
        t = Temperature(32, Scalename.F)
        tp = Temperature(32, Scalename.C)
        self.assertEqual(t.Add(tp).Number, 121.6)
        pass

    #Test To Substract When the scale temperature is   the same
    def test_ToSubstractEqual(self):
        t = Temperature(38, Scalename.F)
        tp = Temperature(32, Scalename.F)
        self.assertEqual(t.Substract(tp).Number, 6)
        pass

    #Test To Substract When the scale temperature is not  the same
    def test_ToSubstractNoEqual(self):
        t = Temperature(100, Scalename.F)
        tp = Temperature(67, Scalename.C)
        self.assertEqual(t.Substract(tp).Number, -52.6)
        pass

    #Test To MultiplyBy When the scale temperature is the same
    def test_MultiplyByEqual(self):
        t = Temperature(4, Scalename.F)
        tp = Temperature(5, Scalename.F)
        self.assertEqual(t.MultiplyBy(tp).Number, 20)
        pass

    #Test To MultiplyBy When the scale temperature is not  the same
    def test_MultiplyByNoEqual(self):
        t = Temperature(4, Scalename.F)
        tp = Temperature(267, Scalename.K)
        self.assertEqual(t.MultiplyBy(tp).Number, 83.72)
        pass

    #Test To DivideBy When the scale temperature is  the same

    def test_DivideByEqual(self):
        t = Temperature(10, Scalename.F)
        tp = Temperature(5, Scalename.F)
        self.assertEqual(t.DivideBy(tp).Number, 2)
        pass

    #Test To DivideBy When the scale temperature is not  the same
    def test_DivideByNoEqual(self):
        t = Temperature(108, Scalename.F)
        tp = Temperature(34, Scalename.C)
        self.assertEqual(t.DivideBy(tp).Number, 1.16)
        pass

    # Test that returns a string of a temperature

    def ToString(self):
        t = Temperature(108, Scalename.F)
        self.assertEqual(t.ToString(), "108F")
        pass

    def test_other(self):
        self.assertTrue(True)
        pass

    def setUp(self):
        pass


def suite():
  return unittest.makeSuite(Instance_test, "test")


def main():
  runner = unittest.TextTestRunner(sys.stdout)
  runner.run(suite())


if __name__ == "__main__":
  main()
