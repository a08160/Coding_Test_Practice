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

# 문제4. 조건 문자열

def solution(ineq, eq, n, m):
    return int(eval(f"{n} {ineq}{eq} {m}".replace("!","")))

'''
eval() 함수는 쓰면 안 되는 것은 아님

간단한 수식에 대한 문자열 등은 eval() 함수를 활용해서 처리하는 것이 효율적임

다만 복잡한 코드의 경우에는 eval()이 하드 코딩화 시킬 가능성이 높아 사용을 지양해야 함

또한, 입력을 그대로 실행하기 때문에 보안상 위험할 수 있음

그리고, 정적 분석(코드의 흐름)을 하기 어려움
'''

def solution(arr, k):
    lst = list(set(arr))
    l = len(lst)
    if l >= k:
        return lst[:k]
    else:
        return lst + [-1]*(k-l)
    

print(solution([0,1,1,1],4 ))

'''
pow(x, y, z): x**y%z
'''