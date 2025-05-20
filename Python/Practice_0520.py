# 문제1. 대소문자 바꿔서 출력하기

str = input()

print(str.swapcase())

'''
str.swapcase(): 대문자는 소문자로, 소문자는 대문자로 바꿔서 출력
'''

# 문제2. 코드 처리하기

def solution(code):
    ret = ''
    mode = 0 
    
    for idx, val in enumerate(code):
        if val == "1":
            mode = abs(mode-1)
            pass
        else:
            if mode == 1 and idx%2 != 0:
                ret += val
                pass
            if mode == 0 and idx%2 == 0:
                ret += val
                pass
    
    if ret:
        return ret
    return "EMPTY"

'''
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
'''

'''
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1  # XOR 연산. mode == 1 이라면 0으로 변경. mode == 0 이라면 1로 변경
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'
'''

# 문제3. 문자 개수 세기

from collections import Counter

def solution(my_string):
    answer = [0]*52
    lst = list(range(65,91))+list(range(97,123))
    dct = dict(Counter(my_string))
    
    for key, val in dct.items():
        answer[lst.index(ord(key))] = val
        
    return answer

'''
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer
'''