

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))


stu1 = Student('stu1', 85)
stu2 = Student('stu2',90)

stu1.print_score()
