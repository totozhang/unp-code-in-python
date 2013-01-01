#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import sys
import socket
import constants as const
from misc import *

if __name__ == '__main__':
    try:
        # This is an AF_INET address defination
        address = (sys.argv[1], 13)
    except IndexError:
        # more pythonic than checking argv length
        err_quit('usage: %s <IPAddress>' % (sys.argv[0]))

    # Creating a socket
    # same like the assignment to sockfd
    # in the original C code
    # I didn't wrap it with try-except because
    # I don't know what exception will be raised here
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    try:
        sockfd.connect(address)
    except socket.error as e:
        err_sys(e, msg='connection error')

    line = sockfd.recv(const.MAXLINE)

    print(line)
