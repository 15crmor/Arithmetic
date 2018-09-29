from fractions import Fraction
import Fractions

class Caculation(object):

    #  计算相应运算符下两参数的值
    def caulate(self, op, f1, f2):
        result = Fractions.Fractions()
        n1 = int(f1.numerator)
        d1 = int(f1.denominator)
        n2 = int(f2.numerator)
        d2 = int(f2.denominator)
        list = []
        if op == '+':
            re = Fraction(n1, d1) + Fraction(n2, d2)

        elif op == '-':
            re = Fraction(n1, d1) - Fraction(n2, d2)

        elif op == '×':
            re = Fraction(n1, d1) * Fraction(n2, d2)

        else:
            re = Fraction(n1, d1) / Fraction(n2, d2)

        return re

    # 比较传入参数大小并返回
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

