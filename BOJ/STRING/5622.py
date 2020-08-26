#-*- encoding: utf-8 -*-
"""다이얼"""
import sys

#strings = sys.stdin.readline().split()
strings = list(str(input()))
sum = 0

for i in range(len(strings)) :
    if strings[i] == 'A' or strings[i] == 'B' or strings[i] == 'C':
        sum += 3
    if strings[i] == 'D' or strings[i] == 'E' or strings[i] == 'F':
        sum += 4
    if strings[i] == 'G' or strings[i] == 'H' or strings[i] == 'I':
        sum += 5
    if strings[i] == 'J' or strings[i] == 'K' or strings[i] == 'L':
        sum += 6
    if strings[i] == 'M' or strings[i] == 'N' or strings[i] == 'O':
        sum += 7
    if strings[i] == 'P' or strings[i] == 'Q' or strings[i] == 'R' or strings[i] == 'S' :
        sum += 8
    if strings[i] == 'T' or strings[i] == 'U' or strings[i] == 'V':
        sum += 9
    if strings[i] == 'W' or strings[i] == 'X' or strings[i] == 'Y' or strings[i] == 'Z':
        sum += 10

print(sum)