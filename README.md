# Py-Promises

## Introduction

The `Promise` class is a basic implementation of Promises pattern in Python. It allows asynchronous execution of functions and provides ways to handle the resolved/rejected promise.

## Class constructor

The constructor of Promise class accepts two parameters:

- `coroutine`: A callable function to be executed asynchronously
- `params`: A list of parameters to be passed to the coroutine function.

## Class Methods

## `all`

`all` is a static method that takes in a list of Promise objects and returns the resolved values of all promises in the same order as the promises were passed to the method.

## `then`

`then` is an instance method that takes two parameters:

- `callback`: A callable function that will be executed when the Promise is resolved.
- `error`: A callable function that will be executed when an error is raised during the execution of coroutine (optional).
  to_thread
  to_thread is an instance method that returns a Thread object with coroutine as the target.

## `wait`

`wait` is an instance method that runs the coroutine and returns the resolved value of the Promise.

# Example Usage

```
def add(a, b):
    return a + b

def handle_success(result):
    print(f'Success: {result}')

def handle_error(error):
    print(f'Error: {error}')

promise = Promise(add, 1, 2)
promise.then(handle_success, handle_error)
```

# Real World Usage Examples

## Sending an Email

```
from pypromises.promise import Promise
import smtplib

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("youremail@gmail.com", "your_email_password")

    message = f"Subject: {subject}\n\n{message}"
    server.sendmail("youremail@gmail.com", receiver, message)
    server.quit()
    return "Email sent successfully"

promise = Promise(send_email, "receiver@gmail.com", "Test Email", "This is a test email")
promise.then(lambda value: print(value), lambda error: print(error))
```

## Uploading a File

```
from pypromises.promise import Promise
import requests

def upload_file(file_path, url):
    with open(file_path, "rb") as file:
        files = {"file": file}
        response = requests.post(url, files=files)
    return response.status_code

promise = Promise(upload_file, "example.txt", "http://localhost:8000/upload")
promise.then(lambda value: print(value), lambda error: print(error))
```

## Processing Large Data

```
from pypromises.promise import Promise

def process_data(data):
    # Perform heavy processing
    return processed_data

promise = Promise(process_data, large_data)
promise.then(lambda value: print(value), lambda error: print(error))
```

## A promise to download a file

```
import requests

def download_file(url):
response = requests.get(url)
return response.content

promise = Promise(download_file, "https://www.example.com/file.txt")

def download_callback(value):
with open("file.txt", "wb") as f:
f.write(value)
print("File has been downloaded and saved")

promise.then(download_callback)
```

## A promise to fetch data from an API

```
import requests

def fetch_data(url):
response = requests.get(url)
return response.json()

promise = Promise(fetch_data, "https://www.example.com/api/data")

def fetch_callback(value):
print("Data:", value)

promise.then(fetch_callback)
```

# Examples By Methods

## Simple promise

```
def greet(name):
    return f"Hello, {name}"

promise = Promise(greet, "John")

def greeting_callback(value):
    print(value)

promise.then(greeting_callback)
```

Output:

```
Hello, John
```

## Promise with error handling

```
def divide(a, b):
    return a / b

promise = Promise(divide, 10, 0)

def success_callback(value):
    print(value)

def error_callback(err):
    print(f"An error occurred: {err}")

promise.then(success_callback, error_callback)
```

Output:

```
An error occurred: division by zero
```

## Promise.all()

```
def fetch_user(id):
    return f"User with id {id} was fetched"

def fetch_post(id):
    return f"Post with id {id} was fetched"

user_promise = Promise(fetch_user, 1)
post_promise = Promise(fetch_post, 2)

values = Promise.all(user_promise, post_promise)
print(values)
```

Output:

```
['User with id 1 was fetched', 'Post with id 2 was fetched']
```

## Using wait method

```
import time

def task(sec):
time.sleep(sec)
return "Task completed"

promise = Promise(task, 1)

result = promise.wait()
print(result)
```

Output:

```
Task completed
```

## Using to_thread method

```
import time

def task(sec):
time.sleep(sec)
return "Task completed"

promise = Promise(task, 1)

thread = promise.to_thread()
thread.start()
thread.join()
print(promise.returned_value)
```

Output:

```
Task completed
```

## Using all method

```
import time

def task_1(sec):
time.sleep(sec)
return "Task 1 completed"

def task_2(sec):
time.sleep(sec)
return "Task 2 completed"

promise_1 = Promise(task_1, 1)
promise_2 = Promise(task_2, 2)

results = Promise.all(promise_1, promise_2)
print(results)
```

Output:

```
['Task 1 completed', 'Task 2 completed']
```
