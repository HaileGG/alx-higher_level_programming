#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_l = []
    for i in range(0, list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong Type")
            d = 0
        except ZeroDivisionError:
            print("Division by 0")
            d = 0
        except IndexError:
            print(Out of Range)
            d = 0
        finally:
            n_l.append(d)
        return (n_l)
