import concurrent
import multiprocessing
import os

# TODO 1 multiprocessing方式创建多进程
# import multiprocessing
# import time
#
#
# # 定义进程执行的函数
# def worker(name, delay):
#     print(f"进程 {name} 启动（PID: {multiprocessing.current_process().pid}）")
#     time.sleep(delay)  # 模拟任务耗时
#     print(f"进程 {name} 结束")
#
#
# if __name__ == "__main__":
#     # Windows 系统必须在 if __name__ == "__main__" 中创建进程（避免重复导入）
#     start_time = time.time()
#
#     # 创建 2 个进程
#     p1 = multiprocessing.Process(target=worker, args=("A", 2))  # args 传参（元组）
#     p2 = multiprocessing.Process(target=worker, kwargs={"name": "B", "delay": 3})  # kwargs 传参
#
#     # 启动进程
#     p1.start()
#     p2.start()
#
#     # 等待进程结束（阻塞主进程）
#     p1.join()
#     p2.join()
#
#     print(f"总耗时：{time.time() - start_time:.2f}s")  # 约 3s（并行执行）


# TODO 进程池 方法 1 进程池方式
# def worker(num):
#     print(f'Worker {num}, PID: {os.getpid()}')
#     return num * 2
#
#
# if __name__ == '__main__':
#     # 创建进程池
#     with multiprocessing.Pool(processes=4) as pool:
#         results = pool.map(worker, range(5))
#         print(f'Results: {results}')


# TODO 进程池 方法 2：concurrent.futures.ProcessPoolExecutor（推荐，更简洁）
from concurrent.futures import ProcessPoolExecutor
import time


def task(num):
    print(f"处理任务 {num}（PID: {multiprocessing.current_process().pid}）")
    time.sleep(1)
    return num * 2


if __name__ == "__main__":
    start_time = time.time()

    # 创建进程池（max_workers 为最大进程数，默认 CPU 核心数）
    with ProcessPoolExecutor(max_workers=3) as executor:
        # 方式 1：map 批量执行（按顺序返回结果）
        results = list(executor.map(task, range(5)))
        print("map 结果：", results)  # [0, 2, 4, 6, 8]
        print("-" * 100)
        # 方式 2：submit 异步提交单个任务（灵活控制）
        futures = [executor.submit(task, i) for i in range(5)]
        # 遍历获取结果（完成一个取一个，不保证顺序）
        for future in concurrent.futures.as_completed(futures):
            print("as_completed 结果：", future.result())

    print(f"总耗时：{time.time() - start_time:.2f}s")  # 约 2s
