import Fractions
import re
import operator

class Judge(object):

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

    def judge(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return 'empty'
        elif tree1 is not None and tree2 is not None:
            if tree1.key != tree2.key:
                return 0
            else:
                if(re.match('\*|\+',tree1.key)):
                    pass
                    #if ((judge(tree1.leftChild,tree2.leftChild)and))





    def isOperator(self, operator):
        if operator == "+" or operator == "-" or operator == "×" or operator == "÷" or operator == "(" or operator == ")":
            return True
        else:
            return False

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