#-*- encoding: utf-8 -*-
"""스택 수열"""
#idea : 입력 값 크기 만큼 for문을 돌면서 입력값을 체크하여 스택에 push,pop 연산

count = 0 # for문 내 입력값과 비교를 위한 counter
stack = [] # stack 리스트
result = [] # '+' or '-'
noFlag = True # 중복되는 숫자 바꿔주기 위한 flag

for i in range(int(input())) :
    num = int(input())

    while count < num : # 입력수가 될 때까지 계속 증가시켜주며 stack에 push함
        count += 1
        stack.append(count)
        result.append('+') #push

    if stack[-1] == num : # 받은 입력 값이 스택의 가장 끝이라면 pop 시켜줌
        stack.pop()
        result.append('-') #pop
    else :
        noFlag = False

if noFlag == False :
    print('NO')
else :
    print('\n'.join(result))


#print(stack)

# 처음시도 - 실패
# for _ in range(size) :
#     numbers.append(int(input()))
#
# print(numbers)

# for i in range(size) :
#     for j in range(len(numbers)) :
#         if i+1 != numbers[j] :
#             if (i+1) not in stack :
#                 stack.append(numbers[j])
#                 print('push')
#             elif (i+1) in stack :
#                 stack.pop(-1)
#                 print('pop')
#         elif i+1 == numbers[i] :
#             stack.pop(-1)
#             print('pop')