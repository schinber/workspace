def outer_func(msg):
    # 外层函数的变量（自由变量）
    message = msg

    # 内层函数（嵌套函数）
    def inner_func():
        # 引用外层函数的变量
        print(message)

    # 返回内层函数（不执行，返回引用）
    return inner_func


# 调用外层函数，接收返回的内层函数
hello_func = outer_func("Hello, Closure!")
# 执行内层函数（此时仍能访问外层的 message 变量）
hello_func()  # 输出：Hello, Closure!

# 再次调用，仍能保留变量环境
hi_func = outer_func("Hi!")
hi_func()  # 输出：Hi!
