import Fractions
from fractions import Fraction
import re
import operator
from BinaryTree import BinaryTree
import Caculation

class Judge(object):

    # 生成逆波兰式
    def toRPN(self, list):
        right = []
        aStack = []
        position = 0
        while True:
            if self.isOperator(list[position]):
                if list == [] or list[position] == "(":
                    aStack.append(list[position])
                else:
                    if list[position] == ")":
                        while True:
                            if aStack != [] and aStack[-1] != "(":
                                operator = aStack.pop()
                                right.append(operator)
                            else:
                                if aStack != []:
                                    aStack.pop()
                                break
                    else:
                        while True:
                            if aStack != [] and self.priority(list[position], aStack[-1]):
                                operator = aStack.pop()
                                if operator != "(":
                                    right.append(operator)
                            else:
                                break
                        aStack.append(list[position])
            else:
                right.append(list[position])
            position = position + 1
            if position >= len(list):
                break
        while aStack != []:
            operator = aStack.pop()
            if operator != "(":
                right.append(operator)
        return right

    #  将逆波兰式转换成二叉树并规范化
    def createTree(self, suffix):
        stacks = []

        for i in range(0, len(suffix)):
            tree = BinaryTree()
            ob = suffix[i]
            c = Caculation.Caculation()
            if self.isOperator(ob):
                t2 = BinaryTree()
                t1 = BinaryTree()
                t2 = stacks.pop()
                t1 = stacks.pop()
                if ob == '-' and t1.value <= t2.value:
                    return None
                else:
                    if self.maxTree(t1, t2):
                        tree.set_date(ob)
                        tree.set_left(t1)
                        tree.set_right(t2)
                        tree.set_value(c.caulate(ob, t1.value, t2.value))
                    else:
                        tree.set_date(ob)
                        tree.set_left(t2)
                        tree.set_right(t1)
                        tree.set_value(c.caulate(ob, t1.value, t2.value))
                    stacks.append(tree)
            else:
                tree.set_value(ob)
                tree.set_date(ob)
                stacks.append(tree)
        return tree

    # 判断是否为符号
    def isOperator(self, operator):
        if operator == "+" or operator == "-" or operator == "×" or operator == "÷" or operator == "(" or operator == ")":
            return True
        else:
            return False

    #  当两颗树value值相等时判定优先级
    def priority(self, operatorout, operatorin):
        m = -1
        n = -1
        addop = [["+", "-", "×", "÷", "(", ")"], ["+", "-", "×", "÷", "(", ")"]]
        first = [[1, 1, 2, 2, 2, 0], [1, 1, 2, 2, 2, 0],
                 [1, 1, 1, 1, 2, 0], [1, 1, 1, 1, 2, 0],
                 [2, 2, 2, 2, 2, 0], [2, 2, 2, 2, 2, 2]]
        for i in range(6):
            if operatorin == addop[0][i]:
                m = i
        for i in range(6):
            if operatorout == addop[1][i]:
                n = i
        if m == -1 and n == -1:
            return False
        elif m == -1 and n != -1:
            return False
        elif m != -1 and n == -1:
            return True
        elif first[m][n] == 1:
            return True
        else:
            return False

    # 判断左右子树
    def maxTree(self, t1, t2):
        c = Caculation.Caculation()
        max = c.max(t1.value, t2.value)  # 比较两个树value值大小
        if max == 1:
            return True
        elif max == 2:
            return False
        elif self.priority(t1.date, t2.date):  # 如果两个树的value值相等，则判定优先级
            if t1.left == None or t2.left == None:
                return True
            max = c.max(t1.left.value, t2.left.value)
            if max == 1:
                return True
            elif max == 2:
                return False
            else:
                return True
        return False
