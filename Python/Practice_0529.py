# 문제1. 성격 유형 검사하기

from collections import defaultdict

def solution(survey, choices):
    survey = [s[1] for s in survey]
    choices = [ c-4 for c in choices]
    
    result_dict = defaultdict(int)
    
    for k, v in zip(survey, choices):
        result_dict[k] += v
    
    answer = ""
    
    for a, b in [("R","T"), ("C","F"), ("J", "M"), ("A", "N")]:
        
        if result_dict[a] >= result_dict[b]:
            answer += a
        else:
            answer += b
            
    return answer

# 문제2. 바탕화면 정리

def solution(wallpaper):
    
    dct = {"x":[],"y":[]}
    
    for i, w in enumerate(wallpaper):
        if '#' in w:
            dct["x"].append(i)
            dct["y"].extend([w.index("#"),w.rindex("#")])
    print(dct)
    return [min(dct["x"]),min(dct["y"]),max(dct["x"])+1,max(dct["y"])+1]

'''
# 최대 최소 좌표를 지속적으로 업데이트
def solution(wallpaper):
    rdx, rdy = 0, 0
    lux, luy = 50, 50
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if j <= lux:
                    lux = j
                if i <= luy:
                    luy = i
                if i+1 >= rdx:
                    rdx = i+1
                if j+1 >= rdy:
                    rdy = j+1


    answer = [luy, lux, rdx, rdy]
    return answer
'''

# 문제3. 개인정보 수집 유효기간

from datetime import datetime

def solution(today, terms, privacies):
    terms = {k: int(t) for k, t in [term.split() for term in terms]}
    privacies = [(k, t) for t, k in [privacy.split() for privacy in privacies]]

    deadlines = []
    for k, t in privacies:
        y, m, d = map(int, t.split("."))
        term = terms[k]

        m += term
        y += (m - 1) // 12
        m = (m - 1) % 12 + 1

        deadlines.append(f"{y}.{m:02}.{d:02}")

    answer = []
    today_date = datetime.strptime(today, "%Y.%m.%d")
    for i, d in enumerate(deadlines):
        deadline_date = datetime.strptime(d, "%Y.%m.%d")
        if today_date >= deadline_date:
            answer.append(i + 1)

    return answer

# 문제4. 가장 많이 받은 선물

def solution(friends, gifts):
    l = len(friends)
    name_index = {name: idx for idx, name in enumerate(friends)}
    total_table = [[0] * l for _ in range(l)]
    quotient_table = [[0] * 3 for _ in range(l)]  # [준 선물, 받은 선물, 차이]

    for a, b in [gift.split() for gift in gifts]:
        a_idx = name_index[a]
        b_idx = name_index[b]

        total_table[a_idx][b_idx] += 1
        quotient_table[a_idx][0] += 1  # 준 선물
        quotient_table[b_idx][1] += 1  # 받은 선물

    for i in range(l):
        quotient_table[i][2] = quotient_table[i][0] - quotient_table[i][1]

    result = [0] * l

    for i in range(l):
        for j in range(i+1, l):
            a = i
            b = j
            if total_table[a][b] > total_table[b][a]:
                result[a] += 1
            elif total_table[a][b] < total_table[b][a]:
                result[b] += 1
            else:
                if quotient_table[a][2] > quotient_table[b][2]:
                    result[a] += 1
                elif quotient_table[a][2] < quotient_table[b][2]:
                    result[b] += 1
                # else: 같으면 선물 없음

    return max(result)

# 문제5. 택배 상자 꺼내기

def solution(n, w, num):
    num -= 1
    nums = list(range(0, n))
    
    lst = [nums[i:i + w] for i in range(0, n, w)]
    idx = lst[num//w].index(num)
    
    return len(list(filter(lambda x: len(x) > idx, lst)))-num//w

'''
def solution(n, w, num):
    m1 = num%(w*2)
    m2 = ((w*2+1) - m1)%(w*2)
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))
'''