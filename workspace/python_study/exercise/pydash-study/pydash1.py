# coding:utf-8
import pydash
from pydash.arrays import iterflatten

a = [0] * 10

b = [1, 3, 5, 9]

print(pydash.nth([1, 2, 3], 0))


def change(x):
    a[x] = 1
    return a


# print map(change, b)
# change(x)
for xi in b:
    a[xi] = 1


def change1(b):
    for xi in b:
        a[xi] = 1
    return a



if __name__ == '__main__':

    iterflatten(array, depth=-1)

    # change(b)
