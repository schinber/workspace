import threading

# 1. 锁
lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:  # 自动获取和释放锁
        counter += 1

# 2. 信号量
semaphore = threading.Semaphore(3)  # 最多3个线程同时访问

# 3. 事件
event = threading.Event()

def wait_for_event():
    print('Waiting for event')
    event.wait()  # 阻塞直到事件被设置
    print('Event received')