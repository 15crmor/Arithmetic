import random
import CreatProblem

class Arith(object):

    def creat(self,problem_number, r):
        creat_pro = CreatProblem.Create()
        file1 = open("Exercises.txt", "w")
        file2 = open("Answer.txt", "w")
        problem_list = []
        num_list = ['`', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '×', '÷']
        num = 0
        while num < problem_number:
            arith = creat_pro.create_arith(r)
            file1.write(creat_pro.to_string(arith) + '\n')
            print(creat_pro.to_string(arith) + '\n')
            num +=1



class Torandom(object):
    def _init_(self,n):
        pass
    def creat(self):
        e1 = random.random()
        e2 = random.random()


a = Arith()
a.creat(10,5)