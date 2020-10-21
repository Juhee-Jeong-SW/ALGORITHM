#위장

def solution(clothes):
    dict = {}
    answer = 1

    for i in range(len(clothes)):
        if clothes[i][1] in dict:
            dict[clothes[i][1]] += 1
        else:
            dict[clothes[i][1]] = 1

    for key in dict:
        answer *= dict[key] + 1

    return answer - 1