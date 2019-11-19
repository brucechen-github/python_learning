from random import randint, sample
from functools import reduce
# print(sample('abcdefg', 3))
# print(sample('abcdefg', randint(3, 6)))

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1)
print(s2)
print(s3)

print(s1.keys() & s2.keys() & s3.keys())

# map & reduce
print(map(dict.keys, [s1, s2, s3]))
r = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))
print(r)