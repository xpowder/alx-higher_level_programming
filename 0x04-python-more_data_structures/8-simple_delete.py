#!/usr/bin/python3
def simple_delete(a_dictionry, key=""):
    if key in a_dictionry:
        del a_dictionry[key]
    return a_dictionry
