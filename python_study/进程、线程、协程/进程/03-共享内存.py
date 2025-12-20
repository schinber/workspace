import multiprocessing


def add_num(shared_num, lock):
    """对共享变量累加（需加锁避免竞争）"""
    current_process = multiprocessing.current_process()
    print(f"进程启动: {current_process.name}, PID: {current_process.pid}")
    for _ in range(100000):
        with lock:  # 上下文管理器自动获取/释放锁
            shared_num.value += 1


if __name__ == "__main__":
    # 创建共享整数（'i' 表示 int 类型，初始值 0）
    shared_num = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()  # 锁：保证共享资源原子操作

    # 创建 2 个进程并发修改
    # 修改进程创建部分
    p1 = multiprocessing.Process(target=add_num, args=(shared_num, lock), name="Process-1")
    p2 = multiprocessing.Process(target=add_num, args=(shared_num, lock), name="Process-2")

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("最终结果：", shared_num.value)  # 200000（无锁可能小于 200000）
