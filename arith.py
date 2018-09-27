import random
import CreatProblem
import Judge
import BinaryTree
import Check
class Arith(object):

    def creat(self,problem_number, r):
        creat_pro = CreatProblem.Create()
        t = BinaryTree.BinaryTree()
        c = Check.Check()
        file1 = open("Exercises.txt", "w")
        file2 = open("Answer.txt", "w")
        problem_list = []
        num_list = ['`', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '×', '÷']
        num = 0
        while num < problem_number:
            arith = creat_pro.create_arith(r)
            Ju = Judge.Judge()
            al = Ju.toRPN(arith)
            string = creat_pro.to_string(creat_pro.proper_fraction(arith))
            ta = Ju.createTree(al)
            if c.check_rpn(t.to_string(ta)):
                file1.write("(%d) " % (num+1) + string + '\n')
                file2.write("(%d) " % (num+1) + str(ta.value) + '\n')
                print(creat_pro.to_string(creat_pro.proper_fraction(arith)) + '\n')
                num +=1



class Torandom(object):
    def _init_(self,n):
        pass
    def creat(self):
        e1 = random.random()
        e2 = random.random()


a = Arith()
a.creat(10000,5)