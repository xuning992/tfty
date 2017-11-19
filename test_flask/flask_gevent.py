# !/usr/bin/python
# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))
from main_flask import application


if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    WSGIServer(("0.0.0.0", 5563), application).serve_forever()
