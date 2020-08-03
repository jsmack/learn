import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,format='%(threadName)s: %(message)s')

#def work1(x,y=2):
#def work1(d, lock):
def work1(lock):
    logging.debug('start')
    with lock:
        lock.acquire()
        i = d['x']
        time.sleep(1)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1

    lock.release()
    logging.debug('end')


#def work2(x,y=2):
#def work2():
def work2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')



if __name__ == '__main__':
    ##threads = []
    ##for _ in range(5):
    #    t = threading.Thread(target=work1)
    #    t.setDaemon(True)
    #    t.start()
    #    threads.append(t)
    ##for thred in threads:
    ##    thred.join()
    #for thread in threading.enumerate():
    #    if thread is threading.currentThread():
    #        print(thread)
    #        continue
    #    thread.join()
    ###t1 = threading.Thread(name='rename work1',target=work1)
    ##t1 = threading.Thread(target=work1)
    ##t1.setDaemon(True)
    ###t2 = threading.Thread(target=work2,args=(100,),kwargs={'y':200})
    ##t2 = threading.Thread(target=work2)
    ##t1.start()
    ##t2.start()
    ##print('started')
    ##t1.join()
    ##t2.join()
    ########
    #t = threading.Timer(3,work2,args=(100,), kwargs={'y': 200})
    #t.start()
    #t.join()

    d = {'x': 0}
    #lock = threading.Lock()
    lock = threading.RLock()
    t1 = threading.Thread(target=work1, args=(d, lock))
    t2 = threading.Thread(target=work2, args=(d, lock))

    t1.start()
    t2.start()
