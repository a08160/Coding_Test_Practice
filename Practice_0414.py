# 문제1. 성격 유형 검사하기(Lv.1)



# 문제2. 바탕화면 정리(Lv.1)


# 문제3. 개인정보 수집 유효기간(Lv.1)



# 문제4. [PCCE 기출문제] 10번 / 공원(Lv.1)



# 문제5. [PCCP 기출문제] 1번 / 동영상 재생기(Lv.1)



# 문제6. 택배 상자 꺼내기(Lv.1)



# 문제7. 가장 많이 받은 선물(Lv.1)


# 문제8. 할인 행사(Lv.2)

from math import ceil

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    cnt = 0
    for product in discount:
        try:
            want_dict[product] -= 1
        except:
            pass

        cnt += 1
        if all(val <= 0 for val in want_dict.values()):
            return ceil(cnt/10)
        
    return 0

print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))


# 문제9. 의상(Lv.2)

from collections import defaultdict

def solution(clothes):
    lst = defaultdict(list)

    for cloth, type in clothes:
        lst[type].append(cloth)
    
    answer = 1

    for items in lst.values():
        answer *= (len(items)+1)

    return answer-1

# Reduce 활용

import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1

# 문제10. 기능 개발(Lv.2)

from math import ceil

def solution(progresses, speeds):
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = []
    current_max = days[0]
    count = 1

    for day in days[1:]:
        if day <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = day
            count = 1
    answer.append(count)
    return answer
