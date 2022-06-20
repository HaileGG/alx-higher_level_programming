#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        d = a / b
    except (TypeError, ZeroDivisionError):
        d = None
    finally:
        print("Inside Result: {}".format(d))
    return (d)
