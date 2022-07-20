#!/usr/bin/python3
"""
Write a python function that takes as parameters a list of integers and a target value,
it sorts the list in ascending order and returns the index if the target is found.
If not, return the index where it would be if it were inserted in order.
"""

def index_find(mylist, target):
    ab = sorted(mylist)
    if target in mylist:
        return ab.index(target)
    else:
        mylist.append(target)
        ab = sorted(mylist)
        return ab.index(target)
