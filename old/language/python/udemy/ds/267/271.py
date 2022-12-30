import asyncio

import multiprocessing
import threading
import time


# generate loop object
loop = asyncio.get_event_loop()

# @asyncio.coroutine
async def worker():
    print('start')
    #time.sleep(2)
    # yield from asyncio.sleep(2)
    await asyncio.sleep(2)
    print('stop')


if __name__ == '__main__':
    loop.run_until_complete(asyncio.wait([worker(),worker()]))
    loop.close()

    #worker()
    # t1 = threading.Thread(target=worker)
    # t2 = threading.Thread(target=worker)
    # t1.start()
    # t2.start()
    #
    # p1 = multiprocessing.Process(target=worker)
    # p2 = multiprocessing.Process(target=worker)
    # p1.start()
    # p2.start()

