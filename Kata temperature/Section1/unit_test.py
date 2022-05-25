from lib2to3.pytree import convert
import unittest
from SectionFirst import Temperature

Obj = Temperature



class TestConversion(unittest.TestCase):

# Celsius to Kelvin
    def test_temperature(self):
        self.assertEqual(Obj.Celsius_to_kelvin(356), 629.15)

 # Celsius to Fahrenheit
    def test_temperatureCF(self):
        self.assertEqual(Obj.Celsius_to_fahrenheit(356), 672.8)

# Fahrenheit to Kelvin
    def test_temperatureFK(self):
        self.assertEqual(Obj.Fahrenheit_to_kelvin(672.8), 629.15)

# Fahrenheit to Celsius
    def test_temperatureFC(self):
        self.assertEqual(Obj.Fahrenheit_to_celsius(672.8), 356)

# Kelvin to Celsius
    def test_temperatureKC(self):
        self.assertEqual(Obj.Kelvin_to_celsius(629.15), 356)

# Kelvin to Fahrenheit
    def test_temperatureKF(self):
        self.assertEqual(Obj.Kelvin_to_fahrenheit(217.15), -68.8)

# Negative Celsius to Kelvin
    def test_temperatureCK(self):
        self.assertEqual(Obj.Celsius_to_kelvin(-56), 217.15)

 #  Negative Celsius to Fahrenheit
    def test_temperaturenegativeCF(self):
        self.assertEqual(Obj.Celsius_to_fahrenheit(-56), -68.8)

# Negative Fahrenheit to Kelvin
    def test_temperaturenegativeFK(self):
        self.assertEqual(Obj.Fahrenheit_to_kelvin(-68.8), 217.15)

# Negative Fahrenheit to Celsius
    def test_temperaturenegativeFC(self):
        self.assertEqual(Obj.Fahrenheit_to_celsius(-68.8), -56)

# 0 Kelvin to Celsius
    def test_temperaturenegativeKC(self):
        self.assertEqual(Obj.Kelvin_to_celsius(217.15), -56)

# Negative Kelvin to Fahrenheit
    def test_temperaturenegtiveKF(self):
        self.assertEqual(Obj.Kelvin_to_fahrenheit(217.15), -68.8)


# 0 Celsius to Kelvin
    def test_temperature0CK(self):
        self.assertEqual(Obj.Celsius_to_kelvin(0),273.15)

 #  Negative Celsius to Fahrenheit
    def test_temperature0CF(self):
        self.assertEqual(Obj.Celsius_to_fahrenheit(0), 32)

# 0 Fahrenheit to Kelvin
    def test_temperature0FK(self):
        self.assertEqual(Obj.Fahrenheit_to_kelvin(0), 255.37)

# 0 Fahrenheit to Celsius
    def test_temperature0FC(self):
        self.assertEqual(Obj.Fahrenheit_to_celsius(0), -17.78)

# 0 Kelvin to Celsius
    def test_temperature0KC(self):
        self.assertEqual(Obj.Kelvin_to_celsius(0), -273.15)

# 0 Kelvin to Fahrenheit
    def test_temperature0KF(self):
        self.assertEqual(Obj.Kelvin_to_fahrenheit(0), -459.67)






        


if __name__ == "__main__":
    unittest.main()
