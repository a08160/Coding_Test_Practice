# 문제1. 체육복(Lv.1)
# Greedy Method(탐욕법)

def solution(n,lost,reserve):
    # 여벌이 있지만 도난당한 학생을 우선 제거
    lost_set = set(lost)-set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 여분이 있을 경우 자신보다 앞쪽 번호의 학생에게 빌려줌
    for r in sorted(reserve_set):
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
        
    return n-len(lost_set)

# 문제2. 크레인 인형뽑기 게임(Lv.1)

import numpy as np

def solution(board, moves):
    board = np.array(board).T.tolist()
    board = [[x for x in col if x != 0] for col in board]

    basket = []
    cnt = 0

    for move in moves:
        col = board[move - 1]
        if col:  # 해당 열이 비어있지 않다면
            doll = col.pop(0)
            if basket and basket[-1] == doll:
                basket.pop()
                cnt += 2
            else:
                basket.append(doll)
    return cnt

def distance(pos, number):
    position = {
        0: [1, 0],
        1: [0, 3],
        2: [1, 3],
        3: [2, 3],
        4: [0, 2],
        5: [1, 2],
        6: [2, 2],
        7: [0, 1],
        8: [1, 1],
        9: [2, 1],
        "*": [0, 0],
        "#": [2, 0]
    }

    return abs(position[pos][0] - position[number][0]) + abs(position[pos][1] - position[number][1])

# 문제3. 키패드 누르기(Lv.1)

def solution(numbers, hand):
    pos = {
        1: (0, 3), 2: (1, 3), 3: (2, 3),
        4: (0, 2), 5: (1, 2), 6: (2, 2),
        7: (0, 1), 8: (1, 1), 9: (2, 1),
        '*': (0, 0), 0: (1, 0), '#': (2, 0)
    }

    left = '*'
    right = '#'
    answer = ""

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            lx, ly = pos[left]
            rx, ry = pos[right]
            nx, ny = pos[number]

            l_dist = abs(lx - nx) + abs(ly - ny)
            r_dist = abs(rx - nx) + abs(ry - ny)

            if l_dist < r_dist:
                answer += 'L'
                left = number
            elif r_dist < l_dist:
                answer += 'R'
                right = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number

    return answer


# 문제4. 성격 유형 검사하기(Lv.1)


# 문제5. 신규 아이디 추천(Lv.1)


# 문제6. 바탕화면 정리(Lv.1)


# 문제7. 개인정보 수집 유효기간(Lv.1)


# 문제8. 달리기 경주(Lv.1)


# 문제9. 유연근무제(Lv.1)


# 문제10. 공원 산책(Lv.1)


# 문제11. [PCCE 기출문제] 10번 / 공원(Lv.1)


# 문제12. [PCCP 기출문제] 1번 / 붕대 감기(Lv.1)


# 문제13. 신고 결과 받기(Lv.1)


# 문제14. [PCCP 기출문제] 1번/ 동영상 재생기(Lv.1)


# 문제15. 택배 상자 꺼내기(Lv.1)


# 문제16. 가장 많이 받은 선물(Lv.1)