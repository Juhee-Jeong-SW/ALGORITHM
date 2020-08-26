#-*- encoding: utf-8 -*-
"""크로아티아 알파벳"""
import re

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = str(input())

for i in cro :
    if i in string :
        string = string.replace(i, " ")

print(len(string))