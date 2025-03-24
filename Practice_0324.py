'''
문제1.
문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
'''

from collections import Counter

def solution(s):
    counter = Counter(s)  # 문자열에서 문자 빈도 계산
    lst = [key for key, value in counter.items() if value == 1]  # 한 번만 등장한 문자만 추출
    return "".join(sorted(lst))  # 사전순으로 정렬 후 문자열 생성

# 다른 사람 풀이

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer