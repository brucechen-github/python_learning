from collections import deque
import pickle

q2 = pickle.load(open('history', 'rb+'))
print(q2)
q = deque([], 5)

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)
q.append(6)
print(q)

pickle.dump(q, open('history', 'wb+'))

from random import randint

N = randint(0, 100)
history = deque([], 10)


def guess(k):
    if k == N:
        print('Bingo')
        return True
    if k < N:
        print('Less')
    else:
        print('Greater')
    return False


while True:
    line = input('Input a random num: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'h':
        print(list(history))
