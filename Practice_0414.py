# 문제1. [1차] 캐시(Lv.2)
'''
캐시 교체 알고리즘: LRU(Least Recently Used)
cache hit: 동일 데이터가 현재 데이터 리스트 내에 있을 때
cache miss

LRU 알고리즘이란? 가장 오래 전에 사용된 데이터를 우선 제거하는 방식
캐시 크기에 따라서 저장 데이터를 최신순으로 관리
'''
def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = []
    time = 0

    for city in cities:
        if city in cache:
            cache.remove(city)      # 기존 위치 제거
            time += 1               # cache hit
        else:
            time += 5               # cache miss

        cache.insert(0, city)       # 최신 사용 데이터를 맨 앞에 추가

        if len(cache) > cacheSize:
            cache.pop()            # 가장 오래된 항목 제거 (맨 뒤)

    return time


# 문제2. 튜플(Lv.2)

def solution(s):
    # 문자열 → 리스트로 변환
    s = s[2:-2].split("},{")  # "2},{2,1},{2,1,3},{2,1,3,4" → 리스트
    s = [list(map(int, group.split(','))) for group in s]

    # 길이 기준으로 정렬 (작은 튜플부터)
    s.sort(key=lambda x: len(x))

    result = []
    for group in s:
        for num in group:
            if num not in result:
                result.append(num)

    return result

        


# 문제3. 프로세스(Lv.2)

# 문제4. 롤케이크 자르기(Lv.2)

def solution(topping):
    cnt = 0

    for idx in range(1,len(topping)-1):
        if len(set(topping[:idx+1])) == len(set(topping[idx:])):
            cnt += 1

    return cnt

print(solution([1,2,3,1,4])) 

# 문제5. [3차] n진수 게임(Lv.2)

def solution(n, t, m, p):
    word = ""
    num = 0

    # n진수 문자열을 t * m 만큼 생성
    while len(word) < t * m:
        word += convert(num, n)
        num += 1

    # 튜브(p)가 말할 숫자들만 뽑기 (p는 1-based index)
    answer = ''
    for i in range(p - 1, t * m, m):
        answer += word[i]

    return answer

# 10진수를 n진수로 변환하는 함수
def convert(num, base):
    chars = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = chars[num % base] + result
        num //= base
    return result


# 문제6. [1차] 뉴스 클러스터링(Lv.2)

from collections import Counter

def make_bigrams(s):
    s = s.lower()
    bigrams = []
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair.isalpha():  # 알파벳 두 글자인 경우만 포함
            bigrams.append(pair)
    return bigrams

def solution(str1, str2):
    c1 = Counter(make_bigrams(str1))
    c2 = Counter(make_bigrams(str2))

    # 교집합, 합집합
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())

    if union == 0:
        return 65536

    return int(intersection / union * 65536)


# 문제7. 피로도(Lv.2)
# 완전 탐색 / DFS 백트래킹

from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for order in permutations(dungeons):
        fatigue = k
        count = 0
        for min_req, cost in order:
            if fatigue >= min_req:
                fatigue -= cost
                count += 1
            else:
                break
        max_count = max(max_count, count)

    return max_count




# 문제8. 할인 행사(Lv.2)

from collections import Counter

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    total_days = len(discount)
    count = 0

    for i in range(total_days - 9):  # 10일 간의 윈도우
        window = discount[i:i+10]
        window_counter = Counter(window)

        # 조건 충족 여부 확인
        if all(window_counter[item] >= want_dict[item] for item in want_dict):
            count += 1

    return count

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
