import multiprocessing


def process_a(pipe):
    pipe.send("来自 A 的消息")  # 发送数据
    print("A 接收：", pipe.recv())  # 接收数据
    pipe.close()


def process_b(pipe):
    print("B 接收：", pipe.recv())  # 接收数据
    pipe.send("来自 B 的回复")  # 发送数据
    pipe.close()


if __name__ == "__main__":
    # 创建管道，返回两个连接对象（conn1, conn2）
    conn1, conn2 = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=process_a, args=(conn1,))
    p2 = multiprocessing.Process(target=process_b, args=(conn2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
