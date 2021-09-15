import time


# 関数を引数にとって inner関数のオブジェクトを返す
def output_work_time(func):
    # どの引数でも対応できるようにこの引数を指定
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before:.2f} sec.")
    return inner

@output_work_time
def lazy_func(sec):
    print(f"I am working so hard...")
    time.sleep(sec)
    print(f"I am finally done!!")




lazy_func(4)