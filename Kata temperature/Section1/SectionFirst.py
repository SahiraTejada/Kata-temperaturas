import math

# Constructor
def __init__(self, number, scaletempearure):
    self.number = number
    self.scaletempearure = scaletempearure

#Conversion for temperatures
class Temperature:

    # Convert from Celsius to Kelvin
    def Celsius_to_kelvin(a):
        conversion = float(a + 273.15)
        result = round(conversion, 2)
        return float(result)

# Convert from Celsius to Fahrenheit
    def Celsius_to_fahrenheit(a):
        conversion = float((a*(9/5))+32)
        result = round(conversion, 2)
        return float(result)

# Convert from Fahrenheit to Celsius
    def Fahrenheit_to_celsius(a):
        conversion = float((a-32) * 5/9)
        result = round(conversion, 2)
        return float(result)

# Convert from Fahrenheit to kelvin
    def Fahrenheit_to_kelvin(a):
        conversion = float((a-32)*(5/9)+ 273.15)
        result = round(conversion, 2)
        return float(result)

# Convert from Kelvin to Celsius
    def Kelvin_to_celsius(a):
        conversion = float(a - 273.15)
        result = round(conversion, 2)
        return float(result)

#Convert from Kelvin to Fahrenheit
    def Kelvin_to_fahrenheit(a):
        conversion = float((a-273.15)*(9/5) + 32)
        result = round(conversion, 2)
        return float(result)

#Operations for the temperatures
class Operations:

#Sum
    def Add(number,a):
        return number + a

#subtraction
    def Substract(number,a):
        return number - a

#Multiplication
    def MultiplyBy(number,a):
        return number * a

#Division
    def DivideBy(number,a):
        return number/a

#Convert to String
    def ToString(a,b):
        return str(a).strip() +  b.strip() 








