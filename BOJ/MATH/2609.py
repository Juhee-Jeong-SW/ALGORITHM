#-*- encoding: utf-8 -*-
"""최대공약수와 최소공배수"""
import sys

n1, n2 = map(int, sys.stdin.readline().split())
r = 0
answer = []

#최대 공약수
def gcd(n1, n2) :
    while n2 != 0 :
        r = n1 % n2
        n1 = n2
        n2 = r

    return n1


answer.append(gcd(n1,n2))

#최소 공배수
def lcm(n1, n2) :
    return int(answer[0] * (n1/answer[0]) * (n2/answer[0]))


answer.append(lcm(n1,n2))

for i in answer :
    print(i)
