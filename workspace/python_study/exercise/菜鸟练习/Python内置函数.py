# coding:utf-8

a = [1, 23, 4, 5, 6]


def get_odd(x):
    if x % 2 != 0:
        return x


b = filter(get_odd, a)


# c = [x*x for x in b]
# c = map(lambda x: x if x >5 else pass , b)
# print c
# print('\n'.join([''.join(['%s*%s=%-2s '%(y,x,x*y)for y in range(1,x+1)])for x in range(1,10)]))

def fun(num):
    return 2 * num - 1


print[fun(x)
for x in range(3, 10)]
