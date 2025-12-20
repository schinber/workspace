import asyncio
import aiohttp  # 异步 HTTP 客户端（需安装：pip install aiohttp）


# 异步请求单个 URL
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return f"{url} → 状态码：{response.status}"


# 并发执行多个协程
async def main():
    urls = [
        "https://www.baidu.com",
        "https://www.baidu.com",
        "https://www.baidu.com"
    ]
    # 创建多个协程对象
    tasks = [fetch_url(url) for url in urls]
    # 并发执行所有任务，等待全部完成（返回结果列表）
    results = await asyncio.gather(*tasks)
    for res in results:
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
