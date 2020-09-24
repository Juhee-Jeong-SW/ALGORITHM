#-*- encoding: utf-8 -*-
"""최소공배수"""

import sys

T = int(sys.stdin.readline())
answers = []


def gcd(a, b) :
    if b == 0 :
        return a
    else :
        return gcd(b, a%b)


for _ in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    answers.append(int((A*B) / gcd(A,B)))

for i in answers :
    print(i)