"""

"""
from queue import Queue, LifoQueue, PriorityQueue

# 基本FIFO队列  先进先出 FIFO即First in First Out,先进先出
# maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉
q = Queue(maxsize=0)

# 写入队列数据
q.put(0)
q.put(1)
q.put(2)
# 输出当前队列所有数据
print(q.queue)
# 删除队列数据，并返回该数据
q.get()
# 输也所有队列数据
print(q.queue)

# ----------------------------------------------------------------------------
# LIFO即Last in First Out,后进先出。与栈的类似，使用也很简单,maxsize用法同上
lq = LifoQueue(maxsize=0)

# 队列写入数据
lq.put(0)
lq.put(1)
lq.put(2)

# 输出队列所有数据
print(lq.queue)
# 删除队尾数据，并返回该数据
lq.get()
# 输出队列所有数据
print(lq.queue)
# ----------------------------------------------------------------------------
# 存储数据时可设置优先级的队列
# 优先级设置数越小等级越高
pq = PriorityQueue(maxsize=0)

# 写入队列，设置优先级
pq.put((9, 'a'))
pq.put((7, 'c'))
pq.put((1, 'd'))

# 输出队例全部数据
print(pq.queue)

# 取队例数据，可以看到，是按优先级取的。
pq.get()
pq.get()
print(pq.queue)
