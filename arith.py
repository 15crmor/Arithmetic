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
        num = 0
        while num < problem_number:
            arith = creat_pro.create_arith(r)
            Ju = Judge.Judge()
            al = Ju.toRPN(arith)
            print(al)
            string = creat_pro.to_string(creat_pro.proper_fraction(arith))
            ta = Ju.createTree(al)
            val = str(creat_pro.pop_fracte(ta.value))
            if c.check_rpn(t.to_string(ta)):
                file1.write("(%d) " % (num+1) + string + '\n')
                file2.write("(%d) " % (num+1) + val + '\n')
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