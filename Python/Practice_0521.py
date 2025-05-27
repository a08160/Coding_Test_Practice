# 문제1. 1로 만들기

def solution(num_list):
    answer = 0
    multiple_2 = [2,4,8,16]
    
    for num in num_list:
        # num보다 큰 multiple_2 원소의 개수를 센다
        count = sum(1 for x in multiple_2 if num >= x)
        answer += count
    
    return answer

'''
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)
'''

# 문제2. 문자열이 몇 번 등장하는 지 세기
# 정규표현식

import re

def solution(myString, pat):
    # (?=...) : 앞서보기 (lookahead)를 사용해 겹치는 패턴도 인식
    pattern = f'(?={re.escape(pat)})'
    return len(re.findall(pattern, myString))

