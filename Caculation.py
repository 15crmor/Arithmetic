from fractions import Fraction
import Fractions

class Caculation(object):

    def caulate(self, op, f1, f2):
        result = []
        n1 = int(f1.numerator)
        d1 = int(f1.denominator)
        n2 = int(f2.numerator)
        d2 = int(f2.denominator)
        if op == '+':
            re = Fraction(n1, d1) + Fraction(n2, d2)
            result.append(re)

        elif op == '-':
            re = Fraction(n1, d1) - Fraction(n2, d2)
            result.append(re)

        elif op == '×':
            re = Fraction(n1, d1) * Fraction(n2, d2)
            result.append(re)

        else:
            re = Fraction(n1, d1) / Fraction(n2, d2)
            result.append(re)


