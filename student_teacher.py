#! /usr/bin/env python3
import sys
from collections import Counter

"""
Counter的用法
Counter("abcaannb").most_common(2) ---对于字符串进行计算，每个字符串有多少个，最多返回两个字符串
[('a',3),('n',2)] ---返回列表，字符与个数用元组表示，无序
"""

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return 0


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year,grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        comm = Counter(self.grade).most_common(4)
        n1=0
        n2=0
        for i in comm:
            if i[0] != 'D':    #这里的每一个i都是一个元组，对他进行索引取值
                n1 += i[1]
            else:
                n2 += i[1]
        print("Pass: {}, Fail: {}".format(n1,n2))

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers,grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        list1 =[]
        comm = Counter(self.grade).most_common(4)
        for i,j in comm:   #这里需要对元组里的两个元素同时进行格式化
            list1.append("{}:{}".format(i,j))   #格式化之后放到列表中 
        print(','.join(list1))


person1 = Person('Sachin')
if sys.argv[1] == 'student':   #sys.argv进行索引取值的时候python3不包含在里面
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_grade()
else:
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    teacher1.get_grade()
