import asyncio


async def slow_task():
    await asyncio.sleep(3)  # 模拟耗时 3 秒的 IO 任务
    return "任务完成"


async def main():
    try:
        # 设置超时 2 秒
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("任务超时！")


asyncio.run(main())  # 输出：任务超时！
