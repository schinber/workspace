import asyncio


# 定义协程
async def coro_demo():
    print("协程启动")
    await asyncio.sleep(1)  # 异步等待 1 秒（非阻塞）
    print("协程恢复")
    return "完成"


# 启动协程（Python 3.7+ 简化写法，无需手动管理事件循环）
result = asyncio.run(coro_demo())
print(f"结果：{result}")
