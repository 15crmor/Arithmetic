import Fractions

class BinaryTree(object):
    def __init__(self):
        pass

    def set_number(self, number):
        self.number = number

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_value(self, value):
        self.valut = value

    def toString(self, tree):
        s = ""
        s = self.outPutTree(tree, s)
        return s

    def outPutTree(self, tree, s):
        if tree != None:
            s1 = self.outPutTree(tree.left,s)
            s2 = self.outPutTree(tree.right,s)

            if type(tree.number) == Fractions.number:
                return str(s1) + str(s2) + str(tree.number.toString())
            else:
                return s

    def createTree(self, exp):
        stack = []
        op = ['+', '-', '×', '÷']
        for i in exp:
            if i not in op:
                tree = BinaryTree()
                stack.append(tree)
