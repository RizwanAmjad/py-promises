from pypromises.promise import Promise
import time


def task_uploading(sec):
    time.sleep(sec)
    return "Uploading Ended"


def task_test(sec):
    time.sleep(sec)
    return "Testing ended"


promise_upload = Promise(task_uploading, 1)
promise_testing = Promise(task_test, 0.5)

promise_upload.then(lambda: print("Upload CB"))
promise_testing.then(lambda: print("Testing CB"))
