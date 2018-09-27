from fractions import Fraction

class Fractions(object):
    def __init__(self):
        self.numerator = None
        self.denominator = None

    def setNumerator(self,numerator):
        self.numerator = numerator

    def setDenominator(self,denominator):
        self.denominator = denominator

    def toString(self):
        a = self.numerator
        b = self.denominator
        return str(Fraction(a, b))

