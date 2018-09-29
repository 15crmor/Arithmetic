import os
class Compare(object):

    #  对两个文件中的答案进行比较并记录
    def grade(self, exercise_file, answer_file):
        correct = []
        wrong = []
        co = 0
        wr = 0
        with open(answer_file, 'r') as f1, open(exercise_file, 'r', encoding='utf-8') as f2:
            answers = f2.readlines()
            line = 0
            for r_answers in f1.readlines():
                if answers[line] == r_answers:
                    co += 1
                    correct.append(line+1)
                else:
                    wr += 1
                    wrong.append(line+1)
                line += 1
        with open('gread.txt', 'w') as f3:
            f3.write(f"Correct: {str(co)} ({', '.join(str(s) for s in correct if s not in [None])})" + '\n')
            f3.write(f"Correct: {str(wr)} ({', '.join(str(s) for s in wrong if s not in [None])})" + '\n')
        print("文件比较完成")

