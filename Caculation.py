from fractions import Fraction
import Fractions

class Caculation(object):

    def caulate(self, op, f1, f2):
        result = Fractions.Fractions()
        n1 = int(f1.numerator)
        d1 = int(f1.denominator)
        n2 = int(f2.numerator)
        d2 = int(f2.denominator)
        list = []
        if op == '+':
            re = Fraction(n1, d1) + Fraction(n2, d2)
            result.setDenominator(re.denominator)
            result.setNumerator(re.numerator)
            list.append(result)

        elif op == '-':
            re = Fraction(n1, d1) - Fraction(n2, d2)
            result.setDenominator(re.denominator)
            result.setNumerator(re.numerator)
            list.append(result)

        elif op == '×':
            re = Fraction(n1, d1) * Fraction(n2, d2)
            result.setDenominator(re.denominator)
            result.setNumerator(re.numerator)
            list.append(result)

        else:
            re = Fraction(n1, d1) / Fraction(n2, d2)
            result.setDenominator(re.denominator)
            result.setNumerator(re.numerator)
            list.append(result)

        return re

    # 比较数字大小
    def max(self, num1, num2):
        n1 = int(num1.numerator)
        d1 = int(num1.denominator)
        n2 = int(num2.numerator)
        d2 = int(num2.denominator)
        m1 = n1 * d2
        m2 = n2 * d1
        if m1 > m2:
            return 1
        elif m1 < m2:
            return 2
        else:
            return 3

