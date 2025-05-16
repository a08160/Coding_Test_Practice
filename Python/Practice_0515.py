# 문제1. 주사위 게임 3

from collections import Counter

def solution(a, b, c, d):
    dct = dict(sorted(Counter([a,b,c,d]).items(), key = lambda x: x[1]))
    size = len(dct)
    lst = list(dct.keys())
    if size == 1:
        return a*1111
    elif size == 4:
        return min([a,b,c,d])
    else:
        if max(dct.values()) == 3:
            return (10*lst[1]+lst[0])**2
        elif min(dct.values()) == 1:
            return lst[0]*lst[1]
        else:
            return (lst[0]+lst[1])*abs(lst[0]-lst[1]) 
        
# 문제2. 원소들의 곱과 합

from math import prod

def solution(num_list):
    return 0 if prod(num_list) > sum(num_list)**2 else 1

'''
from functools import reduce

def solution(num_list):
    total_sum = sum(num_list)
    total_product = reduce(lambda x, y: x * y, num_list)
    return 1 if total_product < total_sum ** 2 else 0
'''

# 문제3. 순서 바꾸기

def solution(num_list, n):
    return (num_list*(n//len(num_list)+2))[n:n+len(num_list)]

# 문제4. 문자열 바꿔서 찾기기

def solution(myString, pat):
    myString = myString.replace("A","b").replace("B","A").upper()
    
    return 1 if pat in myString else 0

'''
def solution(myString, pat):
    # A는 B로, B는 A로 바꾸기
    trans = myString.translate(str.maketrans("AB", "BA"))
    # pat이 포함되어 있으면 1, 아니면 0
    return 1 if pat in trans else 0
'''

'''
str.maketrans("ABC", "DEF") # A->D, B->E, C->F {A: D, B: E, C: F} 의 딕셔너리를 생성

translate()는 문자열의 문자들을 변환 테이블(매핑 딕셔너리)에 따라 바꿔주는 함수
str.translate(변환_테이블)
'''


