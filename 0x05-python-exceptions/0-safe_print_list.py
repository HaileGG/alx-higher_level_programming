#!/usr/bin/python3
#0-safe_print_list.py
#Auth: Haile G.

def safe_print_list(my_list=[], x=0):
    """ Print x elemnts of list.
    Args:
        my_list (list)
    Reurns:
        The number of elements printed.
    """
    rec = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rec += 1
        except IndexError:
            break
    print("")
    return (rec)
