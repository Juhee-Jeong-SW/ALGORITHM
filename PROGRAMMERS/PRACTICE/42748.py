def solution(array, commands):
    answer = []
    temp = []

    for i in range(len(commands)):
        temp = array[(commands[i][0] - 1):commands[i][1]]
        temp.sort()
        # index = commands[i][2]
        answer.append(temp[commands[i][2] - 1])
        # print(index)
        # print(temp)

    # print(answer)

    return answer