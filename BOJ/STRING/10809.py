#-*- encoding: utf-8 -*-
"""알파벳 찾기"""

alphabet = list(str(input()))
answer = []
r_alpha = []
i = 0

for i in range(26) :
    r_alpha.append(chr(97+i))

for j in range(len(r_alpha)) :
    if r_alpha[j] in alphabet :
        answer.append(alphabet.index(r_alpha[j]))
    if r_alpha[j] not in alphabet :
        answer.append(-1)

for i in answer :
    print(i, end = " ")
