#!/usr/bin/python3
import sys

def safe_function(fun, *args):
    try:
        rs = fun(*args)
        return (rs)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), filesys.stderr)
        return (None)
