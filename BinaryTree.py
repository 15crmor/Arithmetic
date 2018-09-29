import Fractions
from fractions import Fraction

# 二叉树
class BinaryTree(object):
    def __init__(self):
        self.date = None
        self.left = None
        self.right = None
        self.value = None

    def tree(self, date, left, right, value):
        self.date = date
        self.left = left
        self.right = right
        self.value = value

    def set_date(self, date):
        self.date = date

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_value(self, value):
        self.value = value

    def to_string(self, tree):
        s = ""
        s = self.out_put_tree(tree, s)
        return s

    def out_put_tree(self, tree, s):
        if tree != None:
            s1 = self.out_put_tree(tree.left, s)
            s2 = self.out_put_tree(tree.right, s)
            if type(tree.date) == Fractions.Fractions:
                return str(s1) + str(s2) + str(tree.date.to_string())
            else:
                return str(s1) + str(s2) + str(tree.date)
        return s
