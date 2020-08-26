#-*- encoding: utf-8 -*-
"""상수"""

import sys

strings = sys.stdin.readline().split()

strings = [int(strings[0][::-1]), int(strings[1][::-1])]

if strings[0] > strings[1] :
    print(strings[0])
if strings[0] < strings[1] :
    print(strings[1])