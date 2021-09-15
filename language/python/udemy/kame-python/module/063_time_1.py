import time

# 1970/1/1 unix time
print(time.time())
# 1631706881.251381

print(time.time()/(60*60*24*365))
# 51.74108682656184

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

before = time.time()
fib(30)
after = time.time()

#print(f'recursive fibonacci took { after - before } sec.')
# recursive fibonacci took 3.0994415283203125e-05 sec.
# e-05 10の-５乗

# 小数点第２まで表示
print(f'recursive fibonacci took { after - before:.2f} sec.')
# recursive fibonacci took 0.46 sec.

