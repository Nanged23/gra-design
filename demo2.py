import datetime
import time


def test_func():
    return datetime.datetime.now()


print(test_func())
time.sleep(2)
print(test_func())
