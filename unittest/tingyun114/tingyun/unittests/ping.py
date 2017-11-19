#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def ping(url):
    """
    :param url: the url need to ping
    :return: True if success. else False
    """
    status = False
    if not os.system('ping -c 1 -W 1 %s &> /dev/null' % url):
        status = True

    return status


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print "Input the url."
        sys.exit(1)

    if ping(sys.argv[1]):
        print "success!!"
    else:
        print "failed!!"
