import random
import math
from fractions import Fraction
# import Fraction

class Create(object):
    # 创建四则运算符号
    def create_operator(self):
        operator = ["+", "-", "×", "÷"]
        return random.choice(operator)

    # 生成四则运算
    def create_arith(self, r):
        x = 0
        list = []
        operator_num = random.randint(1, 3)
        print(operator_num)
        e1 = Create()
        e2 = Create()
        if operator_num == 1:
            list.append(e1.create_number(r))
            list.append(e2.create_operator())
            list.append(e1.create_number(r))
        elif operator_num == 2:
            start = random.randint(0, 2)
            end = 0
            if start > 0:
                end = start + 1
            for i in range(1, 4):
                if i == start:
                    list.append("(")
                list.append(e1.create_number(r))
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
                list.append(e1.create_number(r))
                if i == end:
                    list.append(")")
                list.append(e2.create_operator())
            list.pop()
        else:
            list.append(e1.create_number(r))
            list.append(e2.create_operator())
            list.append(e1.create_number(r))

        # for x in range(0,len(list)):
        #     if list[x] == '-' and list[x-1] < list[x+1]:
        #         a = list[x-1]
        #         list[x-1] = list[x+1]
        #         list[x+1] = a
        return list

    # 将假分数转化为带分数
    def proper_fraction(self, list):
        num = 0
        for fract in list:
            if type(fract) == Fraction:
                n1 = fract.numerator
                n2 = fract.denominator
                if n2 == 1:
                    num += 1
                    continue
                elif n1 > n2:
                    sub = int(n1/n2)
                    n1 = n1 % n2
                    list[num] = '%d%s%d/%d' %(sub, '’', n1,n2)
            num += 1
        return list

    # 将答案假分数转化为带分数
    def pop_fracte(self, re):
        n1 = re.numerator
        n2 = re.denominator
        if n2 == 1:
            return n1
        elif n1 < n2:
            return re
        else:
            sub = int(n1/n2)
            n1 = n1 % n2
            return '%d%s%d/%d' % (sub, '’', n1, n2)

    # 生成随机数
    def create_number(self, r):
        b = random.randint(1, r)
        a = random.randint(1, b * r - 1)
        n = Fraction(a, b)
        return n

    # 将列表中的表达式转化成字符串
    def to_string(self, list):
        np = ""
        for i in range(len(list)):
             np = np + str(list[i])
        return np
