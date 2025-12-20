import multiprocessing


def producer(queue):
    """生产者：向队列放入数据"""
    for i in range(5):
        queue.put(f"数据 {i}")
        print(f"生产者放入：数据 {i}")


def consumer(queue):
    """消费者：从队列获取数据"""
    while True:
        data = queue.get()  # 队列为空时阻塞
        if data is None:  # 接收结束信号
            break
        print(f"消费者获取：{data}")


if __name__ == "__main__":
    # 创建队列（默认无界，可指定 maxsize 限制容量）
    queue = multiprocessing.Queue()

    # 创建生产者和消费者进程
    p_producer = multiprocessing.Process(target=producer, args=(queue,))
    p_consumer = multiprocessing.Process(target=consumer, args=(queue,))

    p_producer.start()
    p_consumer.start()

    p_producer.join()  # 等待生产者完成
    queue.put(None)  # 发送结束信号
    p_consumer.join()
