#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from functools import wraps

def exe_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        r = func(*args, **kwargs)
        print('')
        print ">>>>>>>>>>>>>>> %s.%s execution time：%.3fs " % (func.__module__, func.__name__, time.time() - t0)
        print('')
        return r
    return wrapper