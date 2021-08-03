import logging
import queue
import time
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)

def worker1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break

        queue.task_done()
        logging.debug(item)
    logging.debug('loggggggggggggggggggggggg')
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(1000000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')
    for _ in range(3):
        queue.put(None)

    [t.join() for t in ts]
