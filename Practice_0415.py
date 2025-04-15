# 문제1. 성격 유형 검사하기(Lv.1)



# 문제2. 바탕화면 정리(Lv.1)



# 문제3. 개인정보 수집 유효기간(Lv.1)



# 문제4. [PCCE 기출문제] 10번 / 공원(Lv.1)



# 문제5. [PCCP 기출문제] 1번 / 동영상 재생기(Lv.1)



# 문제6. 택배 상자 꺼내기(Lv.1)



# 문제7. 가장 많이 받은 선물(Lv.1)



# 문제8. k진수에서 소수 개수 구하기(Lv.2)

def solution(n,k):
    

# 문제9. [3차] 압축(Lv.2)

def solution(msg):
    # 1. 사전 초기화
    dictionary = {chr(i + 64): i for i in range(1, 27)}  # 'A'~'Z' : 1~26
    next_index = 27
    answer = []

    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1

        # 2. 사전에 등록된 가장 긴 문자열 찾기
        while j <= len(msg) and msg[i:j] in dictionary:
            w = msg[i:j]
            j += 1

        # 3. 정답에 색인 번호 추가
        answer.append(dictionary[w])

        # 4. 새로운 문자열을 사전에 추가
        if j <= len(msg):
            dictionary[msg[i:j]] = next_index
            next_index += 1

        i += len(w)

    return answer


        

# 문제10. 파괴되지 않은 건물(Lv.3)

import numpy as np

def solution(board, skills):
    board = np.array(board)

    for type_, r1, c1, r2, c2, degree in skills:
        sign = -1 if type_ == 1 else 1
        board[r1:r2+1, c1:c2+1] += sign * degree

    return np.sum(board > 0)

# 효율성 강화. Imos Method(Cumsum의 역할 이해하기)

import numpy as np

def solution(board, skills):
    n, m = len(board), len(board[0])
    acc = np.zeros((n+1, m+1), dtype=int)

    for type_, r1, c1, r2, c2, degree in skills:
        sign = -1 if type_ == 1 else 1
        acc[r1][c1] += sign * degree
        acc[r1][c2+1] -= sign * degree
        acc[r2+1][c1] -= sign * degree
        acc[r2+1][c2+1] += sign * degree

    # 가로 방향 누적합
    acc = np.cumsum(acc, axis=1)
    # 세로 방향 누적합
    acc = np.cumsum(acc, axis=0)

    # board에 적용
    board = np.array(board)
    board += acc[:n, :m]

    return np.sum(board > 0)

# Numpy 제외

def solution(board, skills):
    n, m = len(board), len(board[0])
    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for type_, r1, c1, r2, c2, degree in skills:
        sign = -degree if type_ == 1 else degree
        acc[r1][c1] += sign
        acc[r1][c2 + 1] -= sign
        acc[r2 + 1][c1] -= sign
        acc[r2 + 1][c2 + 1] += sign

    # 누적합 (가로 → 세로)
    for i in range(n + 1):
        for j in range(1, m + 1):
            acc[i][j] += acc[i][j - 1]
    for j in range(m + 1):
        for i in range(1, n + 1):
            acc[i][j] += acc[i - 1][j]

    # board에 적용 + 양수 개수 세기
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                count += 1

    return count