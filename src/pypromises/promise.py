from threading import Thread
from typing import Callable, Any, List


class Promise:
    def __init__(self, coroutine: Callable, *params: List[Any]):
        def coroutine_wrapper():
            self.returned_value = coroutine(*params)

        self.returned_value: Any = None
        self.coroutine: Callable = coroutine_wrapper
        self.params: List[Any] = params

    def wait(self):
        Thread(target=self.coroutine).run()
        return self.returned_value
