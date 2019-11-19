from random import randint
from collections import Counter
import re

data = [randint(0, 20) for _ in range(30)]
print(data)

c = dict.fromkeys(data, 0)
print(c)

for x in data:
    c[x] += 1
print(c)

# ======================
c2 = Counter(data)
# 因为是随机的，可能没有 12
# print(c[12])

print(c2.most_common(3))

# ===============
# 词频统计
txt = open('../resouces/english_word.txt').read()
print(txt)

print(re.split('\W+', txt))
c3 = Counter(re.split('\W+', txt))
print(c3)