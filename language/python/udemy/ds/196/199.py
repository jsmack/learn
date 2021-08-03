from multiprocessing import (
    Process,
    Lock,RLock,Semaphore,Queue,Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

def worker1(i):
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')
    return i * 2

if __name__ == '__main__':
    i = 10
    with multiprocessing.Pool(3) as p:
        r = p.imap(worker1,[100,200])
        #r = p.map_async(worker1,[100,200])
        #r = p.map(worker1,[100,200])
        logging.debug('executed')
        logging.debug([ i for i in r])
        # p1 = p.apply_async(worker1, (100,))
        # p2 = p.apply_async(worker1, (100,))
        # logging.debug('execute')
        # logging.debug(p1.get())
        # logging.debug(p2.get())
