# #第1种写法 通过常量定义
# NAME = 0
# AGE = 1
# SEX =2
# =====================
# 第2种写法
NAME, AGE, SEX = range(3)

student = ("bruce", 16, 'male')

print(student[NAME])
print(student[AGE])
print(student[SEX])

# =================
# 通过namedtuple
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex'])
s = Student('chen', 18, 'male')
print(s.name)
