# -*- coding: utf-8 -*-


from flask import Flask
import time


application = Flask(__name__)


@application.route('/normal/a')
def normal():
    time.sleep(3)
    return "ok"


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=10001, debug=True)

