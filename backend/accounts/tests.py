from django.test import TestCase

# Create your tests here.
import asyncio
import time
import requests
async def fetch_data(url):
    # 模拟异步操作，例如发送HTTP请求并获取响应数据
    res = requests.get('http://www.baidu.com')
    print(res)
    # print(url)
    await asyncio.sleep(3)
    # time.sleep(3)
    return "Data from {}".format(url)


async def main():
    # 创建多个异步任务
    task1 = fetch_data("https://example.com")
    task2 = fetch_data("https://google.com")
    task3 = fetch_data("https://google.com")
    task4 = fetch_data("https://google.com")
    task5 = fetch_data("https://google.com")
    print('#')
    # 等待多个异步任务完成，并获取结果
    result1 = await task1
    result2 = await task2
    result3 = await task3
    result4 = await task4
    result5 = await task5

    # 处理结果
    print(result1)
    print(result2)
    print(result5)


# 运行异步代码
asyncio.run(main())
