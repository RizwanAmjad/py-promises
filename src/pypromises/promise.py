from .fire_and_forget import fire_and_forget
from threading import Thread
from typing import Any, Callable, List


class Promise:
    def __init__(self, coroutine: Callable, *params: List[Any]):
        def coroutine_wrapper():
            self.returned_value = coroutine(*params)
            return self.returned_value

        self.returned_value: Any = None
        self.coroutine: Callable = coroutine_wrapper
        self.params: List[Any] = params

    @staticmethod
    def all(*promises: List["Promise"]):
        """
        Return the value from all the promises in given sequence
        params:
        - promises: List of Promises to resolve
        """
        threads = [promise.to_thread() for promise in promises]
        # start all threads
        [thread.start() for thread in threads]
        # wait for all threads to complete
        [thread.join() for thread in threads]

        return [promise.returned_value for promise in promises]

    def then(self, callback: Callable, error: Callable = lambda: None) -> None:
        """
        runs the function wrapped in the promise async, 
        and calls the callback function passed in case of
        promise resolved and runs the error function in case of error raised
        params:
        - callback: Callable (Run in case the promise is resolved)
        - error: Callable (Runs in case the promise is rejected)
        """
        @fire_and_forget
        def cb():
            try:
                value = self.coroutine()
                callback(value)
            except Exception as ex:
                if (error != None):
                    error(ex)
                else:
                    raise ex
        cb()

    def to_thread(self) -> Thread:
        return Thread(target=self.coroutine)

    def wait(self):
        """
        Awaits a promise, the lines next to this function call won't execute until execution of this promise completes
        """
        self.to_thread().run()
        return self.returned_value
