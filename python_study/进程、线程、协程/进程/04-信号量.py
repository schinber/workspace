import multiprocessing
import time


def access_resource(name, semaphore):
    semaphore.acquire()  # 获取信号量（无可用则阻塞）
    print(f"进程 {name} 访问资源")
    time.sleep(1)  # 模拟资源占用
    print(f"进程 {name} 释放资源")
    semaphore.release()  # 释放信号量


if __name__ == "__main__":
    semaphore = multiprocessing.Semaphore(2)  # 允许最多 2 个进程同时访问
    processes = [
        multiprocessing.Process(target=access_resource, args=(f"P{i}", semaphore))
        for i in range(5)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
