#! python3.6
import random
import CreatProblem
import CreateTree
import BinaryTree
import Check
import Compare
import sys
import getopt

class Arith(object):

    # 生成问题和答案在判重后写入文件
    def creat(self, problem_number, r):
        creat_pro = CreatProblem.Create()
        t = BinaryTree.BinaryTree()
        c = Check.Check()
        with open("Exercises.txt", "w") as file1, open("Answer.txt", "w") as file2:
            num = 0
            while num < problem_number:
                arith = creat_pro.create_arith(r)  # 生成四则运算列表
                Ju = CreateTree.Judge()
                al = Ju.toRPN(arith)  # 将列表转换成逆波兰式
                string = creat_pro.to_string(creat_pro.proper_fraction(arith))
                ta = Ju.createTree(al)  # 将逆波兰式生成规范二叉树
                if ta:
                    val = str(creat_pro.pop_fracte(ta.value))
                    if c.check_tree(t.to_string(ta)):  # 进行判重
                        file1.write("%d. " % (num+1) + string + '\n')
                        file2.write("%d. " % (num+1) + val + '\n')
                        num +=1
        print("四则运算题目生成完毕，数量为%d个" % problem_number)

    # 支持命令行键入参数
    def main(self, arith, argv):
        problem_number = None
        num_range = None
        exercise_file = None
        answer_file = None
        try:
            opts, args = getopt.getopt(argv, "n:r:e:a:")
        except getopt.GetoptError:
            print('Error: arith.py -n <problem_number> -r <num_range>')
            print('   or: test_arg.py -e -e <exercisefile>.txt -a <answerfile>.txt')
            sys.exit(2)

        for opt, arg in opts:
            if opt in("-n"):
                problem_number = int(arg)
            elif opt in ("-r"):
                num_range = int(arg)
            elif opt in("-e"):
                exercise_file = arg
            elif opt in("-a"):
                answer_file = arg
        if problem_number and num_range:
            arith.creat(problem_number, num_range)
        elif exercise_file and answer_file:
            compare = Compare.Compare()
            compare.grade('ReAnswer.txt', 'Answer.txt')
        else:
            print('Error: arith.py -n <problem_number> -r <num_range>')
            print('   or: test_arg.py -e -e <exercisefile>.txt -a <answerfile>.txt')



if __name__ == "__main__":
    arith = Arith()
    arith.main(arith, sys.argv[1:])




