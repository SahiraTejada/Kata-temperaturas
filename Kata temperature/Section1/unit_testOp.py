from lib2to3.pytree import convert
import unittest
from SectionFirst import Operations


Obj= Operations

class testOp(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(Obj.Add(10,20),30)

    def test_subtract(self):
        self.assertEqual(Obj.Substract(45,34),11)

    def test_Multiple(self):
        self.assertEqual(Obj.MultiplyBy(5,5,),25)

    def test_Divide(self):
        self.assertEqual(Obj.DivideBy(10,2),5)

    def test_Tostring(self):
        self.assertEqual(Obj.ToString(32,"K"),"32K")    

if __name__ == "__main__":
    unittest.main()        