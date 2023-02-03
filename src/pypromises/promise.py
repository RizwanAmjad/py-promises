from threading import Thread
from typing import Any, Callable, List


class Promise:
    def __init__(self, coroutine: Callable, *params: List[Any]):
        def coroutine_wrapper():
            self.returned_value = coroutine(*params)

        self.returned_value: Any = None
        self.coroutine: Callable = coroutine_wrapper
        self.params: List[Any] = params

    @staticmethod
    def all(*promises: List["Promise"]):
        threads = [promise.to_thread() for promise in promises]
        # start all threads
        [thread.start() for thread in threads]
        # wait for all threads to complete
        [thread.join() for thread in threads]

        return [promise.returned_value for promise in promises]

    def then(self, callback: Callable) -> None:
        def cb():
            self.coroutine()
            callback()
        Thread(target=cb).start()

    def to_thread(self) -> Thread:
        return Thread(target=self.coroutine)

    def wait(self):
        self.to_thread().run()
        return self.returned_value
