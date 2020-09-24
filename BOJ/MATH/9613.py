#-*- encoding: utf-8 -*-
"""GCD 합"""

import sys


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


T = int(sys.stdin.readline())
nums = []
answers = []

for _ in range(T) :
    sums = 0
    nums = list(map(int, sys.stdin.readline().split()))

    n = nums[0]
    lists = nums[1:]

    for i in range(0, n-1) :
        for j in range(i+1, n) :
            sums += gcd(lists[i], lists[j])

    answers.append(sums)

for i in answers:
    print(i)