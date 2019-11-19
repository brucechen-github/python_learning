print(sorted([9, 1, 3, 2, 7, 5]))

# 使用sorted对字典进行排序

from random import randint

names = ['bruce', 'john', 'lili', 'cindy', 'tony']
d = {x: randint(60, 100) for x in names}
print(d)

# 1.转换成元祖
print(sorted(zip(d.values(), d.keys())))

# 2.
print(d.items())
print(sorted(d.items(), key=lambda x: x[1]))
