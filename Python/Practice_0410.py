# 문제1. [1차] 다트 게임(Lv.1)

import re

def solution(dartResult):
    # 1. 정규식으로 올바르게 잘라내기
    results = re.findall(r'\d{1,2}[SDT][*#]?', dartResult)
    scores = []

    for i, res in enumerate(results):
        # 숫자 추출
        num = int(re.match(r'\d{1,2}', res).group())
        # 보너스 처리
        if 'D' in res:
            num **= 2
        elif 'T' in res:
            num **= 3
        # 옵션 처리
        if '*' in res:
            num *= 2
            if i > 0:
                scores[i-1] *= 2
        elif '#' in res:
            num *= -1
        scores.append(num)

    return sum(scores)

'''
* 정규표현식(re)에 대한 이해

\w 문자
\s 공백
\t tab \n new line \r return
\d 숫자
^ 시작 $ 끝  예외) [^cmb] 에서의 ^는 not의 의미. 즉, cmb 모두 포함하지 않을 것을 명령령
. 하나의 character(new line 제외)

* / +
*: 바로 앞의 문자가 0 이상 반복
+: 바로 앞의 문자가 1 이상 반복

ct => ca*t: Yes
   => ca+t: No

{}
Ex. {m,n} 바로 앞의 문자를 m~n회 반복(m이상 n이하)

위 정규 표현식 해석. r'\d{1,2}[SDT][*#]?'

\d{1,2}: 한 자리 또는 두 자리 숫자
[]: ~ 중 하나 => [SDT]: S / D / T 중 하나가 있어야 함
? 있어도 되고 없어도 됨 => [*#]?: * / # 중 하나가 있어도 되고 없어도 됨됨

* re 모듈의 기능

1. c = re.search(r'찾으려는 패턴', '대상 문자열')
: 패턴을 찾으면 match 객체 반환 / 못하면 None 반환

2. c.start() 발견된 첫번째 인덱스 / c.end() 발견된 마지막 인덱스 / c.group(): 검색된 객체 가져오기

3. findall() / finditer()
: 정규식과 매치되는 모든 문자열을 리스트 / 반복 가능한 객체로 리턴 
'''

# 문제2. 로또의 최고 순위와 최저 순위(Lv.1)

def solution(lottos, win_nums):
    zero_num = lottos.count(0)
    win_cnt = len(set(lottos) & set(win_nums))  # 교집합

    # 순위는 맞춘 개수에 따라 7 - 개수 (단, 최소 1등까지고 6등 이하 = 6위)
    best = 7 - (win_cnt + zero_num)
    worst = 7 - win_cnt

    return [best if best < 7 else 6, worst if worst < 7 else 6]

# 다른 풀이. 딕셔너리의 알고리즘 활용

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# 문제3. 문자열 나누기(Lv.1)

def solution(s):
    lst = list(s)
    result = 0

    while lst:
        # 예외 처리: 문자열이 1글자 남았을 때
        if len(lst) == 1:
            result += 1
            break

        target = lst[0]
        for i in range(2, len(lst) + 1, 2):  # 짝수 단위로 탐색
            if lst[:i].count(target) == i // 2:
                result += 1
                lst = lst[i:]
                break
        else:
            # 위 조건을 끝까지 못 찾은 경우 → 남은 거 그냥 하나로 처리
            result += 1
            break  # 더 탐색할 필요 없음

    return result


# 다른 풀이1. 반복문 활용

def solution(s):
    result = 0
    same = 0
    diff = 0
    target = s[0]

    for i in s:
        if i == target:
            same += 1
        else:
            diff += 1

        if same == diff:
            result += 1
            same = 0
            diff = 0
            if i != target:
                target = i

    if same != 0 or diff != 0:
        result += 1

    return result

# 다른 풀이2. deque 활용

from collections import deque

def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans

# 문제4. 둘만의 암호(Lv.1)

def solution(s, skip, ind):

    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    result = ""
    length= len(alphabet)

    for w in s:
        result += alphabet[(alphabet.index(w)+ind)%length]

    return result

# 문제5. 대충 만든 자판(Lv.1)

from collections import Counter

def solution(keymap, targets):
    result = []

    for w in targets:
        cnt = 0
        dct = Counter(w)
        for char, freq in dct.items():
            try:
                min_presses = min([k.index(char) + 1 for k in keymap if char in k])
                cnt += min_presses * freq
            except ValueError:
                cnt = -1
                break
        result.append(cnt)

    return result

# 문제6. [PCCE 기출문제] 9번 / 이웃한 칸(Lv.1)

def solution(board, h, w):
    target = board[h][w]
    position = [[h-1, w], [h+1, w], [h, w-1], [h, w+1]]
    cnt = 0
    
    for i, j in position:
        if 0 <= i < len(board) and 0 <= j < len(board[0]):  # Ensure indices are within bounds
            if board[i][j] == target:
                cnt += 1
    
    return cnt

# 문제7. 완주하지 못한 선수(Lv.1)

def solution(participant, completion):
    for p in completion:
        participant.remove(p)

    return participant[0]

# 효율성 업그레이드 버전

def solution(participant, completion):
    from collections import defaultdict

    # 참가자 이름을 카운트하는 딕셔너리
    participant_count = defaultdict(int)

    # 참가자 명단에 이름을 카운트
    for name in participant:
        participant_count[name] += 1

    # 완주자 명단에 있는 이름은 카운트에서 차감
    for name in completion:
        participant_count[name] -= 1

    # 카운트가 1로 남아 있는 사람이 완주하지 못한 사람
    for name, count in participant_count.items():
        if count > 0:
            return name
        
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    

# 문제8. 햄버거 만들기(Lv.1)

def solution(ingredient):
    ingredient = "".join(map(str,ingredient))
    cnt = 0
    while "1231" in ingredient:
        cnt += 1
        ingredient = ingredient.replace("1231","",1)
    
    return cnt

# 스택 방식 풀이

def solution(ingredient):
    stack = []
    cnt = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            stack[-4:] = []
            cnt += 1
    return cnt

# 문제9. 숫자 짝궁(Lv.1)

from collections import Counter

def solution(X, Y):
    answer = {}
    result = ""

    X_dct, Y_dct = Counter(X), Counter(Y)

    for key in X_dct.keys():
        if key in Y_dct:
            answer[key] = min(X_dct[key], Y_dct[key])

    if not answer:
        return "-1"

    # 숫자 내림차순 정렬
    for key, val in sorted(answer.items(), reverse=True):
        result += key * val

    # 예외 처리: 결과가 0으로만 구성된 경우
    if result[0] == "0":
        return "0"

    return result

    
print(solution("100","2345"))

# 문제10. [PCCE 기출문제] 10번 / 데이터 분석(Lv.1)

def solution(data, ext, val_ext, sort_by):
    dct = {'code':0, 'date':1,'maximum':2,'remain':3}
    index = dct[ext]
    
    data = sorted(filter(lambda x: x[index] < val_ext, data),key = lambda x: x[dct[sort_by]])

    return data