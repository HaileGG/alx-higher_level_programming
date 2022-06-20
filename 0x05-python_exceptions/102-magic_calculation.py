#!/usr/bin/python3
def magic_calculation(a, b):
    re = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                rs += a ** b / i
        except:
            rs = b + a
            break
        return (rs)
