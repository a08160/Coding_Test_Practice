# 문제1. 소수 찾기

from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for div in range(2, int(num**0.5) + 1):
        if num % div == 0:
            return False
    return True

def solution(numbers):
    cases = set()

    # 1부터 전체 길이까지 모든 순열 조합 생성
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int("".join(perm))
            cases.add(num)

    # 소수 개수 세기
    return sum(1 for num in cases if is_prime(num))


# 문제2. 스킬 트리(Lv.2)

def solution(skill, skill_trees):
    lst = list(skill)
    cnt = 0

    for tree in skill_trees:
        intersection_ordered = [char for char in tree if char in lst]
        if skill.find("".join(intersection_ordered)) == 0:
            cnt += 1

    return cnt


# 문제3. [3차] 압축(Lv.2)

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


# 문제4. 파괴되지 않은 건물(Lv.3)

import numpy as np

def solution(board, skills):
    board = np.array(board)

    for type_, r1, c1, r2, c2, degree in skills:
        sign = -1 if type_ == 1 else 1
        board[r1:r2+1, c1:c2+1] += sign * degree

    return np.sum(board > 0)


# 효율성 강화. Imos Method(Cumsum의 역할 이해하기)
'''
Numpy는 기본적으로 C 언어 기반으로 작성되었기 때문에 시간 효율성이 떨어질 수 밖에 없음
따라서 모듈을 import 하지 않고 구현하는 것이 더욱 시간 효율적일 수 있음
'''
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