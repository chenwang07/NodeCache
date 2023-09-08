
from typing import Any
from DependencyGraph import dependencyGraph

class Node:
    def __get__(self, obj, objtype):
        #obj = EquityOptionPricing
        import functools
        return functools.partial(self.__call__, obj)

    def __init__(self, m) -> None:
        self.func = m
        self.need_update = True
        self.name = m.__name__
        self.cache = None

    def __call__(self, p) -> Any:
        if self.need_update:
            print(" get result from calculation")
            res = self.func(p)
            self.cache = res
            self.need_update = False
            return res
        else:
            print(" get result from cache")
            return self.cache




