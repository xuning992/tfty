# -#- coding: utf-8 -*-
activate_this = "/home/nb/virenv/flask_env/bin/activate"
execfile = (activate_this, dict(__file__=activate_this))

import sys

sys.path.insert(0, "/home/nb/webapps/tfty/test_flask")  #工程根目录，即wsgi文件路径

from main_flask import application as application
