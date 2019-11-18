from random import randint
# Python3 用range; Python2 用xrange
data = [randint(-10, 10) for _ in range(10)]
print(data)
result = filter(lambda x: x >= 0, data)
print(result)

# ====================
# 列表解析
result = [x for x in data if x >= 0]
print(result)

# TODO timeit用法
# timeit filter(lambda x: x >= 0, data)

# =============================

d = {x: randint(60, 100) for x in range(1, 21)}
print(d)
# 字典解析
# Python3 用d.items(); Python2 用d.iteritems()
result = {k: v for k, v in d.items() if v > 90}
print(result)

#====================
# 集合解析
s = set(data)
result = {x for x in s if x % 3 == 0}
print(result)
