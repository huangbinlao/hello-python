# -*- coding:utf-8 -*-
import asyncio
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from helloSleep()
    print(r)
    print("Hello again!")

@asyncio.coroutine
def helloSleep():
    print('helloSleep')
    return 'xxx'

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()