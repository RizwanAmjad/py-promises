from pypromises.promise import Promise
import time


def task_uploading(sec):
    time.sleep(sec)
    return "Uploading Ended"


def task_test(sec):
    time.sleep(sec)
    return "Testing ended"


promise_upload = Promise(task_uploading, 0.5)
promise_testing = Promise(task_test, 1)

print(promise_upload.wait())
print(promise_testing.wait())
