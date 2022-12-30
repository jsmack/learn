import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%Y/%m/%d %H:%M:%S'))

print(datetime.date.today().strftime('%Y/%m/%d %H:%M:%S'))


print(datetime.time(hour=1,minute=10,second=5))

print(now + datetime.timedelta(weeks=1))

import time
# Epoc time
print(time.time())