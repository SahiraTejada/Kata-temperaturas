from __future__ import annotations
from enum import Enum

class Scalename(Enum):
    C = 1,
    F = 2,
    K = 3

class Temperature():
    result =  0
    conversion = 0
    number = None
    scaleTemperature = None
    #Constructor
    def __init__(self,number : float,scaleTemperature : Scalename) -> None:

        self.Number = number
        self.ScaleTemperature = scaleTemperature
        
    
    #Convert to Celsius
    def ToCelsius(self):
 
        if(self.ScaleTemperature.name == Scalename.K.name):
           result = self.Number- 273.15
           conversion = round(result,2)
        elif(self.ScaleTemperature.name == Scalename.F.name):
            result = (self.Number-32)*(5/9)
            conversion = round(result, 2)
        return Temperature(conversion, Scalename.C)

        #Convert to Farenheit
    def ToFarenheit(self):

        if(self.ScaleTemperature.name == Scalename.C.name):
           result = self.Number *(9/5) + 32
           conversion = round(result,2)

        elif(self.ScaleTemperature.name == Scalename.K.name):
            result = (self.Number-273.15)*(9/5) + 32
            conversion = round(result, 2)

        return Temperature(conversion, Scalename.F)

        #Convert to Kelvin
    def ToKelvin(self):

        if(self.ScaleTemperature.name == Scalename.C.name):
           result = self.Number + 273.15
           conversion = round(result, 2)
        elif(self.ScaleTemperature.name == Scalename.F.name):
            result = (self.Number-32)*(5/9) + 273.15
            conversion = round(result, 2)

        return Temperature(conversion , Scalename.K)





    #Sum

    def Add(self,other: Temperature):
        first = self.Number
        second = other.Number
        firstTemp = self.ScaleTemperature
        secondTemp = other.ScaleTemperature
    #No equal
        if(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.F):
            second = (second-32)*(5/9)
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.K):
            second = second - 273.15
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.C):
            second = second * (9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.K):
            second = (second-273.15)*(9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.F):
            second = (second-32)*(5/9) + 273.15
            conversion = round(second, 2)
        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.C):
            second = second + 273.15
            conversion = round(second, 2)
        #Equal
        else:
            conversion = second
        return Temperature(round((first + conversion), 2), firstTemp)

    #Substract
    def Substract(self, other: Temperature):
        first = self.Number
        second = other.Number
        firstTemp = self.ScaleTemperature
        secondTemp = other.ScaleTemperature
    #No equal
        if(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.F):
            second = (second-32)*(5/9)
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.K):
            second = second - 273.15
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.C):
            second = second * (9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.K):
            second = (second-273.15)*(9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.F):
            second = (second-32)*(5/9) + 273.15
            conversion = round(second, 2)
        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.C):
            second = second + 273.15
            conversion = round(second, 2)
        #Equal
        else:
            conversion = second
        return Temperature(round((first - conversion),2), firstTemp)

    #Multiplicaction
    def MultiplyBy(self, other: Temperature):
        first = self.Number
        second = other.Number
        firstTemp = self.ScaleTemperature
        secondTemp = other.ScaleTemperature
    #No equal
        if(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.F):
            second = (second-32)*(5/9)
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.K):
            second = second - 273.15
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.C):
            second = second * (9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.K):
            second = (second-273.15)*(9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.F):
            second = (second-32)*(5/9) + 273.15
            conversion = round(second, 2)
        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.C):
            second = second + 273.15
            conversion = round(second, 2)
        #Equal
        else:
            conversion = second
        return Temperature(round((first * conversion),2), firstTemp)
    #Division
    def DivideBy(self, other: Temperature):
        first = self.Number
        second = other.Number
        firstTemp = self.ScaleTemperature
        secondTemp = other.ScaleTemperature
    #No equal
        if(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.F):
            second = (second-32)*(5/9)
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.C and secondTemp == Scalename.K):
            second = second - 273.15
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.C):
            second = second * (9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.F and secondTemp == Scalename.K):
            second = (second-273.15)*(9/5) + 32
            conversion = round(second, 2)

        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.F):
            second = (second-32)*(5/9) + 273.15
            conversion = round(second, 2)
        elif(firstTemp != other.Number and firstTemp == Scalename.K and secondTemp == Scalename.C):
            second = second + 273.15
            conversion = round(second, 2)
        #Equal
        else:
            conversion = second
        return Temperature(round((first / conversion),2), firstTemp)

    # Convert to a string
    def ToString(self):
        return (self.Number).strip() + str(self.ScaleTemperature).strip()



        






