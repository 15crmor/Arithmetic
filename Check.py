class Check(object):

    def __init__(self):
        self.check = []

    #  对二叉树进行判重
    def check_tree(self, tree):
        if self.check == []:
            self.check.append(tree)
            return True
        else:
            for i in range(len(self.check)):
                if self.check[i] == tree:
                    return False
        self.check.append(tree)
        return True
