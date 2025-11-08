import time


def func_cost(func):
    """
    时间统计装饰器函数
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} 执行时间: {execution_time} 秒")
        return result

    return wrapper