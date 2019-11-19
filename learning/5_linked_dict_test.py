d = {}
d['Jimmy'] = (1, 35)
d['bruce'] = (2, 37)
d['tom'] = (3, 40)
d['ss'] = (4, 49)
for k in d: print(k)

# 有序
from collections import OrderedDict

d = OrderedDict()
d['Jimmy'] = (1, 35)
d['bruce'] = (2, 37)
d['tom'] = (3, 40)
d['ss'] = (4, 49)
for k in d: print(k)

# ---------------------

from time import time
from random import randint

d = OrderedDict()
players = list('ABCDEFGH')
start = time()
for i in range(8):
    input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, p, end - start)
    d[p] = (i + 1, end - start)

print()
print('-' * 20)
for k in d:
    print(k, d[k])
