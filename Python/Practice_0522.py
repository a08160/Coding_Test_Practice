# 문제1. 특정 문자열로 끝나는 가장 긴 부분 찾기

def solution(myString, pat):
    myString, pat = myString[::-1], pat[::-1]
    idx = myString.find(pat)
    
    return myString[idx:][::-1] # rfind의 기능을 find로 구현한 형태


'''
solution=lambda x,y:x[:x.rindex(y)+len(y)]

* find와 index의 차이
find는 찾는 문자열이 없을 경우 -1을 반환하고, index는 ValueError를 발생시킴

find는 문자열(string) 전용, index는 iterable 객체 모두에 사용 가능
'''

# 문제2. 문자열 묶기

from collections import Counter

def solution(strArr):
    length_counts = Counter(len(s) for s in strArr)
    sorted_lengths = sorted(length_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_lengths[0][1]

'''
from collections import Counter

def solution(strArr):
    length_counts = Counter(len(s) for s in strArr)
    
    return max(length_counts.values())
'''

# 문제3. 2의 영역

def solution(arr):
    
    if 2 not in arr:
        return [-1]
    
    r = arr[::-1].index(2)
    l = arr.index(2)

    return arr[l:len(arr)-r]

print("!@#$%^&*\(\\'\"<>?:;")