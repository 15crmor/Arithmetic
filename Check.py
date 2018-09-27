class Check(object):

    def __init__(self):
        self.check = []
        self.repeat_no = 0

    def check_rpn(self,list):
        if self.check == []:
            self.check.append(list)
            return True
        else:
            for i in range(len(self.check)):
                if self.check[i] == list:
                    self.repeat_no = i
                    self.check.append(list)
                    return False
        self.check.append(list)
        return True