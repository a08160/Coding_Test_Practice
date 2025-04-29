# 문제1. 2016년(Lv.1)

from datetime import datetime

def solution(a,b):
    start = datetime(2016,1,1)
    target = datetime(2016,a,b)

    dct = {0:"FRI",1:"SAT",2:"SUN",3:"MON",4:"TUE",5:"WED",6:"THU"}

    return dct[(target-start).days%7]

# 문제2. 기사단원의 무기(Lv.1)

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 2 if i != n // i else 1  # 제곱수일 경우 중복 제거
    return count

def solution(number, limit, power):
    total_weight = 0
    for i in range(1, number + 1):
        div_count = count_divisors(i)
        if div_count > limit:
            total_weight += power
        else:
            total_weight += div_count
    return total_weight

# 문제3. 모의고사(Lv.1)

from math import ceil
import numpy as np

def solution(answers):
    answers = np.array(answers)
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([2, 1, 2, 3, 2, 4, 2, 5])
    c = np.array([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    length = len(answers)

    a = (a * ceil(length / len(a)))[:length]
    b = (b * ceil(length / len(b)))[:length]
    c = (c * ceil(length / len(c)))[:length]

    score_a = (a == answers).sum()
    score_b = (b == answers).sum()
    score_c = (c == answers).sum()

    scores = [score_a, score_b, score_c]
    max_score = max(scores)

    return [i + 1 for i, s in enumerate(scores) if s == max_score]

# 다른 풀이

def solution(answers):
    # 수포자들이 찍는 방식
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 정답 개수 저장할 리스트
    scores = [0, 0, 0]

    # 각 수포자의 찍기 패턴을 반복하여 정답과 비교
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            scores[0] += 1
        if answers[i] == two[i % len(two)]:
            scores[1] += 1
        if answers[i] == three[i % len(three)]:
            scores[2] += 1

    # 가장 높은 점수 계산
    max_score = max(scores)

    # 가장 높은 점수를 받은 사람(1번부터 시작)들을 리스트에 담아 반환
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return result

# 문제4. 과일 장수(Lv.1)

def solution(k, m, score):
    box = len(score)//m
    result = 0
    score.sort(reverse = True)

    for i in range(box):
        result += score[m*(i+1)-1]*m

    return result

# 다른 사람 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

# 문제5. 덧칠 하기(Lv.1)

def solution(n, m, section):
    answer = 0
    i = 0

    while i < len(section):
        # i번째부터 롤러로 m칸 칠함
        paint_start = section[i]
        paint_end = paint_start + m - 1
        answer += 1

        # i를 롤러가 닿지 않는 다음 위치로 이동
        while i < len(section) and section[i] <= paint_end:
            i += 1

    return answer

# 문제6. 소수 찾기(Lv.1)

def solution(n):
    if n < 2:
        return 0

    primes = [2]
    for i in range(3, n+1, 2):
        is_prime = True
        for j in range(3, int(i**0.5)+1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return len(primes)

# 다른 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# 문제7. 소수 만들기(Lv.1)

from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            count += 1
    return count

# 문제8. 옹알이(2) (Lv.1)
# all 은 모든 조건이 참인 지를 판별함
# any 는 하나라도 참이 되는 지를 판별

def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    count = 0

    babbling = list(filter(lambda x: all(w*2 not in x for w in word), babbling))
    print(babbling)

    for b in babbling:
        temp = b

        for w in word:
            temp = temp.replace(w," ")
        
        if temp.strip() == "":
            count += 1
    
    return count

# 문제9. 실패율(Lv.1)

def solution(N, stages):
    result = []
    total_players = len(stages)
    
    for stage in range(1, N + 1):
        # 현재 스테이지에 머무르고 있는 사람 수
        failed = stages.count(stage)
        
        # 실패율 계산 (도달한 유저가 0이면 0)
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = failed / total_players
        
        result.append((stage, fail_rate))
        
        # 다음 스테이지부터는 현재 스테이지 클리어한 사람만 남음
        total_players -= failed

    # 실패율 기준으로 정렬 (내림차순), 같으면 스테이지 번호 오름차순
    result.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 결과에서 스테이지 번호만 추출
    return [stage for stage, _ in result]
   

# 문제10. [PCCE 기출문제] 9번 / 지폐 접기

def solution(wallet, bill):
    count = 0

    wallet.sort()
    bill.sort()

    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[1] = bill[1]//2
        count+=1
        bill.sort()

    return count

# 문제11. n^2 배열 자르기(Lv.2)

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
    return answer

# 문제12. H-Index(Lv.2)

def solution(citations):
    num = len(citations)

    for h in range(num,0,-1):
        if sum([i>=h for i in citations]) >= h:
            return h
    return 0

# 문제13. 야근 지수(Lv.3)
'''
야근 피로도 += 남은 일의 작업량^2
'''
def solution(n, works):

    if sum(works) <= n:
        return 0
    
    for i in range(n):
        works[works.index(max(works))] -= 1

    return sum([i**2 for i in works])

# 위 코드는 효율성 측면에서 매우 부적절함
    
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0  # 다 끝낼 수 있는 경우 피로도는 0

    # 최대 힙 만들기 (음수 사용)
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        max_work = heapq.heappop(works)
        heapq.heappush(works, max_work + 1)  # 1 줄이기 (음수니까 +1)

    return sum(w**2 for w in works)

'''
* heapq 클래스
가장 작은 값이나 가장 큰 값이 루트로 오게 하는 이진 트리의 자료 구조

주요 함수

heapq.heapify(lst)	기존 리스트를 힙으로 바꿉니다 (제자리 정렬).
heapq.heappush(heap, item)	힙에 아이템을 추가합니다.
heapq.heappop(heap)	가장 작은 원소를 제거하고 반환합니다.
heapq.heappushpop(heap, item)	새 아이템을 넣고, 가장 작은 아이템을 꺼냅니다 (더 빠름).
heapq.heapreplace(heap, item)	heappop 후 heappush (단, 더 빠르게 동작).
heapq.nlargest(n, iterable)	n개의 가장 큰 요소를 반환합니다.
heapq.nsmallest(n, iterable)	n개의 가장 작은 요소를 반환합니다.
'''