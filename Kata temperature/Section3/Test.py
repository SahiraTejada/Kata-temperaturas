import sys
import unittest
from main import *
from Scale import *


class Instance_test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Instance_test, self).__init__(*args, **kwargs)
        self.attribute = Temperature
        self.scale = Scalename

    def test_ToKelvinF(self):
        a = Temperature(34, Scalename.F)
        self.assertEqual(a.ToKelvin().Number, 274.26)
        pass

    def test_ToKelvinC(self):
        a = Temperature(56, Scalename.C)
        self.assertAlmostEquals(a.ToKelvin().Number, 329.15)
        pass

    def test_ToCelsiusK(self):
        a = Temperature(100, Scalename.K)
        self.assertAlmostEquals(a.ToCelsius().Number, -173.15)
        pass

    def test_ToCelsiusF(self):
        a = Temperature(78, Scalename.F)
        self.assertEqual(a.ToCelsius().Number, 25.56)
        pass

    def test_ToFarenheitC(self):
        a = Temperature(69, Scalename.C)
        self.assertEqual(a.ToFarenheit().Number, 156.2)
        pass

    def test_ToFarenheitK(self):
        a = Temperature(302, Scalename.K)
        self.assertEqual(a.ToFarenheit().Number, 83.93)
        pass

    def test_AddEqual(self):
        a = Temperature(34, Scalename.F)
        b = Temperature(34, Scalename.F)
        self.assertEqual(a.Add(b).Number, 68)
        pass

    def test_AddNoEqual(self):
        a = Temperature(34, Scalename.C)
        b = Temperature(56, Scalename.F)
        self.assertEqual(a.Add(b).Number, 47.33)
        pass

    def test_SubstractEqual(self):
        a = Temperature(300, Scalename.K)
        b = Temperature(100, Scalename.K)
        self.assertEqual(a.Substract(b).Number, 200)
        pass

    def test_SubstractNoEqual(self):
        a = Temperature(300, Scalename.K)
        b = Temperature(100, Scalename.C)
        self.assertEqual(a.Substract(b).Number, -73)
        pass

    def test_DivideByEqual(self):
        a = Temperature(100, Scalename.F)
        b = Temperature(50, Scalename.F)
        self.assertEqual(a.DivideBy(b).Number, 2)
        pass

    def test_DivideByNoqual(self):
        a = Temperature(78, Scalename.C)
        b = Temperature(45, Scalename.F)
        self.assertAlmostEquals(a.DivideBy(b).Number, 10.8)
        pass

    def test_MultiplyByEqual(self):
        a = Temperature(30, Scalename.K)
        b = Temperature(10, Scalename.K)
        self.assertEqual(a.MultiplyBy(b).Number, 300)

        pass

    def test_MultiplyByNoEqual(self):
        a = Temperature(5, Scalename.F)
        b = Temperature(280, Scalename.K)
        self.assertEqual(a.MultiplyBy(b).Number, 221.65)
        pass

    def test_ToStrgingTest(self):
        a = Temperature(34, Scalename.C)
        self.assertEqual(a.ToString(), "34C")
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
