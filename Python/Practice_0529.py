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