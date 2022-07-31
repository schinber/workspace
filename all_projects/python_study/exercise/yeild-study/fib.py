def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


# for n in fab(5):
#     print(n)

# ------------------------------------

r_100 = range(100)


# def get_old(x):
#     print("enter func inner...")
#     while x < 100:
#         if x % 2 != 0:
#             yield x
#             x += 1


# g = get_old(10)
# print(next(g))

# for y in get_old(5):
#     print(y)
# ------------------------------------
# s = "ABC"
# l = list-study(s)
# print(l)
# l1 = iter(l)
# print(l1)

def foo():
    print('Starting.....')
    while True:
        res = yield 4
        print("res:", res)


# 下面调用函数并没有执行，可以先将后面的语句注释掉
# 逐行运行代码观察效果
g = foo()
print("第一次调用执行结果：")
print(next(g))
print("*" * 100)

print("第二次调用执行结果：")
print(next(g))
print("*" * 100)
