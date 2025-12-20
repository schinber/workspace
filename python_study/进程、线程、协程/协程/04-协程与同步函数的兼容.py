import asyncio
import requests  # 同步 HTTP 库（阻塞）

"""
如果需要调用同步的 IO 函数（如 requests、sqlite3），
直接调用会阻塞线程，需用 loop.run_in_executor() 将其放到线程池/进程池执行。
"""

# 同步函数（阻塞线程）
def sync_fetch(url):
    response = requests.get(url)
    return f"{url} → 状态码：{response.status_code}"


# 异步包装同步函数
async def async_fetch(url):
    loop = asyncio.get_running_loop()
    # 提交同步函数到线程池执行，避免阻塞事件循环
    result = await loop.run_in_executor(None, sync_fetch, url)
    return result


async def main():
    urls = ["https://www.baidu.com", "https://www.github.com"]
    tasks = [async_fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
