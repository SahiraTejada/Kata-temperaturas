from __future__ import annotations
from Scale import *


class Temperature():
    result = 0
    number = None
    scaleTemp = None
   #Constructor
    def __init__(self,number : float,scaleTemp: Scalename) -> None:
        self.Number = number
        self.ScaleTemp = scaleTemp
        pass

   #Convert to Kelvin
    def ToKelvin(self):
        if(self.ScaleTemp.name == Scalename.C.name):
           result = self.Number + 273.15
        elif(self.ScaleTemp.name == Scalename.F.name):
            result = (5/9)*(self.Number - 32) + 273.15
        return Temperature(round(result,2),Scalename.K.name)

   #Convert to Celsius
    def ToCelsius(self):
        if(self.ScaleTemp.name == Scalename.K.name):
           result = self.Number - 273.15

        elif(self.ScaleTemp.name == Scalename.F.name):
            result = (5/9)*(self.Number - 32)
        return Temperature(round(result, 2), Scalename.C.name)

    #Convert to Farenheit
    def ToFarenheit(self):
        if(self.ScaleTemp.name == Scalename.C.name):
           result = (9/5)*(self.Number) + 32

        elif(self.ScaleTemp.name == Scalename.K.name):
            result = (self.Number-273.15)*(9/5) + 32
        return Temperature(round(result, 2), Scalename.F.name)

    def Add(self, other: Temperature):
        LValue = self.Number
        RValue = other.Number
        RTemp = other.ScaleTemp 
        LTemp = self.ScaleTemp
        # No Equal
        if (RTemp == Scalename.C and LTemp == Scalename.F):
            RValue = RValue * (9/5) + 32
        elif (RTemp == Scalename.C and LTemp == Scalename.K):
            RValue = RValue + 273

        elif (RTemp == Scalename.F and LTemp == Scalename.K):
            RValue = (RValue-32)*(5/9) + 273.15

        elif (RTemp == Scalename.F and LTemp == Scalename.C):
            RValue = (RValue-32)*(5/9)

        elif (RTemp == Scalename.K and LTemp == Scalename.C):
            RValue = RValue - 273

        elif (RTemp == Scalename.K and LTemp == Scalename.F):
            RValue = (RValue-273.15)*(9/5)+32
        # Equal
        else:
            RValue = RValue

        return Temperature(round((LValue + RValue), 2), LTemp)

    def DivideBy(self, other: Temperature):
        LValue = self.Number
        RValue = other.Number
        RTemp = other.ScaleTemp
        LTemp = self.ScaleTemp
        # No Equal
        if (RTemp == Scalename.C and LTemp == Scalename.F):
            RValue = RValue * (9/5) + 32
        elif (RTemp == Scalename.C and LTemp == Scalename.K):
            RValue = RValue + 273

        elif (RTemp == Scalename.F and LTemp == Scalename.K):
            RValue = (RValue-32)*(5/9) + 273.15

        elif (RTemp == Scalename.F and LTemp == Scalename.C):
            RValue = (RValue-32)*(5/9)

        elif (RTemp == Scalename.K and LTemp == Scalename.C):
            RValue = RValue - 273

        elif (RTemp == Scalename.K and LTemp == Scalename.F):
            RValue = (RValue-273.15)*(9/5)+32
        # Equal
        else:
            RValue = RValue

        return Temperature(round((LValue / RValue), 2), LTemp)

    def Substract(self, other: Temperature):
        LValue = self.Number
        RValue = other.Number
        RTemp = other.ScaleTemp
        LTemp = self.ScaleTemp
        #No Equal
        if (RTemp == Scalename.C and LTemp == Scalename.F):
            RValue = RValue * (9/5) + 32
        elif (RTemp == Scalename.C and LTemp == Scalename.K):
            RValue = RValue + 273

        elif (RTemp == Scalename.F and LTemp == Scalename.K):
            RValue = (RValue-32)*(5/9) + 273.15

        elif (RTemp == Scalename.F and LTemp == Scalename.C):
            RValue = (RValue-32)*(5/9)

        elif (RTemp == Scalename.K and LTemp == Scalename.C):
            RValue = RValue - 273

        elif (RTemp == Scalename.K and LTemp == Scalename.F):
            RValue = (RValue-273.15)*(9/5)+32
        # Equal
        else:
            RValue = RValue

        return Temperature(round((LValue - RValue), 2), LTemp)

    def MultiplyBy(self, other: Temperature):
        LValue = self.Number
        RValue = other.Number
        RTemp = other.ScaleTemp
        LTemp = self.ScaleTemp
        #No Equal
        if (RTemp == Scalename.C and LTemp == Scalename.F):
            RValue = RValue * (9/5) + 32
        elif (RTemp == Scalename.C and LTemp == Scalename.K):
            RValue = RValue + 273

        elif (RTemp == Scalename.F and LTemp == Scalename.K):
            RValue = (RValue-32)*(5/9) + 273.15

        elif (RTemp == Scalename.F and LTemp == Scalename.C):
            RValue = (RValue-32)*(5/9)

        elif (RTemp == Scalename.K and LTemp == Scalename.C):
            RValue = RValue - 273

        elif (RTemp == Scalename.K and LTemp == Scalename.F):
            RValue = (RValue-273.15)*(9/5)+32
        # Equal
        else:
            RValue = RValue

        return Temperature(round((LValue * RValue), 2), LTemp)

    def ToString(self):

        return str(self.Number).strip() + str(self.ScaleTemp.name).strip()



