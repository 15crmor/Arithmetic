import random
import math
from fractions import Fraction
import Fraction

class Create(object):
    # 创建四则运算符号
    def create_operator(self):
        operator = ["+", "-", "×", "÷"]
        return random.choice(operator)

    # 生成四则运算
    def create_arith(self):
        list = []
        operator_num = random.randint(1, 3)
        e1 = Create()
        e2 = Create()
        if operator_num == 1:
            list.append(e1.create_number())
            list.append(e2.create_operator())
            list.append(e1.create_number())
        elif operator_num == 2:
            start = random.randint(0, 2)
            end = 0
            if start > 0:
                end = start + 1
            for i in range(1, 4):
                if i == start:
                    list.append("(")
                list.append(e1.create_number())
                if i == end:
                    list.append(")")
                list.append(e2.create_operator())
                list.pop()
        elif operator_num == 3:
            start = random.randint(0, 3)
            end = 0
            if start > 0:
                end = start + 1 + random.randint(0, 1)
                if end >= 4:
                    end = 4
            for i in range(1, 5):

                if i == start:
                    list.append("(")
                list.append(e1.create_number())
                if i == end:
                    list.append(")")
                list.append(e2.create_operator())
            list.pop()
        else:
            list.append(e1.create_number())
            list.append(e2.create_operator())
            list.append(e1.create_number())

        return list

    # 创建数字
    def create_number(self):
        n = Fraction.Fraction()
        b = random.randint(1, 9)
        a = random.randint(1, b * 10 - 1)
       # n = Fraction(a, b)
        tmp = Create()
        divisor = tmp.get_max_divisor(a, b)
        a = a / divisor
        b = b / divisor
        n.setNumerator(a)
        n.setDenominator(b)
        return n

        # 求最大公约数
    def get_max_divisor(self, numerator, denominator):

        return math.gcd(numerator,denominator)


        # 约分
    def reduction(self, fraction):
        a = fraction.numerator
        b = fraction.denominator
        divisor = Create.get_max_divisor(a, b)
        a = a / divisor
        b = b / divisor
        fraction.setNumerator(a)
        fraction.setDenominator(b)
        return fraction

n = Create()
print(n.create_arith())