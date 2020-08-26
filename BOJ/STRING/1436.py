#-*- encoding: utf-8 -*-
"""영화감독 숌"""

number = int(input()) #입력값
macro = 666 #찾을 값
count = 0 #몇번째

while True : # 만족할 때까지 계속 돈다
    if '666' in str(macro) : # 매크로를 계속 증가시키는 동안 666을 만나게 된다면
        count += 1 # 단계수 증가시키기
    if count == number : # 만약 단계수와 입력값인 몇 번째인지를 찾아내는 숫자가 같다면
        print(macro) # 매크로가 무슨 숫자인지를 출력
        break
    macro += 1 #매크로를 증가시키며 훑어야하기 때문에 계속 1씩 증가시켜준다.
