#-*- encoding: utf-8 -*-
"""나머지"""

import sys

A, B, C = map(int, sys.stdin.readline().split(' '))
answers = []

answers.append((A+B) % C)
answers.append(((A%C)+(B%C))%C)

answers.append((A*B) % C)
answers.append(((A%C)*(B%C))%C)

for i in answers:
    print(i)