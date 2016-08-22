'''Created on 2013-5-26'''

import copy
from copy import deepcopy

gstr = "global string"


def func1(i, info):
    x = 12345
    print(locals())


func1(1, "first")

if __name__ == "__main__":
    print("the current scope's global variables:")
    dictionary = globals()
    print(dictionary)