import asyncio
import time


# 模拟一个“慢任务”——点外卖需要 3 秒
async def order_food(food: str):
    print(f"开始点 {food}...")
    await asyncio.sleep(3)  # 模拟等待送餐
    print(f"{food} 已经送到了！")
    return food


# 异步主函数
async def main():
    start = time.time()

    # 并发执行：两份外卖同时在送
    task1 = asyncio.create_task(order_food("披萨"))
    task2 = asyncio.create_task(order_food("汉堡"))


    print("下单完成，可以先刷会儿抖音...")
    food1 = await task1
    food2 = await task2

    print(f"吃到 {food1} 和 {food2} 了！")
    end = time.time()
    print(f"总共花费 {end - start:.2f} 秒")


# 运行异步程序
if __name__ == "__main__":
    asyncio.run(main())
