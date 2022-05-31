#!/usr/bin/python3
for i in range(0, 9 + 1):
    for j in range(i + 1, 9 + 1):
        if (i == and j == 9):
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end='')
