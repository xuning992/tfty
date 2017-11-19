# coding: utf-8


import time


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


def do_something():
    import random
    n = random.randint(2.0, 16.0)
    s = 2 if n >= 4 else n
    time.sleep(s)
    item = fib(n)
    return s, item