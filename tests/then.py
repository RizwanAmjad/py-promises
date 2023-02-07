from pypromises.promise import Promise
import time


def task_uploading(sec):
    time.sleep(sec)
    return "Uploading Ended"


def task_test(sec):
    time.sleep(sec)
    return "Testing ended"


def error_task(message, secs):
    time.sleep(secs)
    raise Exception(message)


promise_upload = Promise(task_uploading, 1)
promise_testing = Promise(task_test, 0.5)
promise_error = Promise(error_task, "Hahah", 0.5)

promise_upload.then(lambda value: print(value))
promise_testing.then(lambda value: print(value))
promise_error.then(lambda value: print(value), lambda err: print(err))
