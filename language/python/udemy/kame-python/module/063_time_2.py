from functools import lru_cache
import time

@lru_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

before = time.time()
fib(30)
after = time.time()

print(f'recursive fibonacci took {after - before:.2f} sec.')
# recursive fibonacci took 0.00 sec.


# c.time() current local time
print(time.ctime())
# Wed Sep 15 21:04:14 2021


localtime = time.localtime()
print(localtime)
# time.struct_time(tm_year=2021, tm_mon=9, tm_mday=15, tm_hour=21, tm_min=4, tm_sec=14, tm_wday=2, tm_yday=258, tm_isdst=0)

print(localtime.tm_year)
# 2021

print("{0.tm_year} {0.tm_mon}".format(localtime))
# 2021 9

sec = 10
before = time.time()
time.sleep(sec)
after = time.time()
print(f'{after - before}')
# 10.003956079483032

