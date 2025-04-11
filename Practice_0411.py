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

# 문제4. [PCCP 기출문제] 1번 / 붕대 감기(Lv.1)

def solution(bandage, health, attacks):
    end_time = attacks[-1][0]
    attack = {i:j for i,j in attacks}
    show_time, recover, plus = bandage[:]
    cnt = 0 
    heart = health

    for time in range(1, end_time+1):
        try:
            heart -= attack[time]
            cnt = 0

            if heart <= 0:
                return -1
        except:
            cnt += 1
            heart += recover

            if show_time == cnt:
                heart += plus
                cnt = 0
        
        if heart > health:
            heart = health
        
    return heart

# 문제5. 신규 아이디 추천(Lv.1)

def solution(new_id):
    

# 문제6. 바탕화면 정리(Lv.1)


# 문제7. 개인정보 수집 유효기간(Lv.1)


# 문제8. 달리기 경주(Lv.1)


# 문제9. 유연근무제(Lv.1)

def solution(schedules, timelogs, startday):
    def add_10_minutes(time):
        hour = time // 100
        minute = time % 100 + 10
        if minute >= 60:
            hour += 1
            minute -= 60
        return hour * 100 + minute

    # 각 스케줄에 10분 추가
    schedules = [add_10_minutes(schedule) for schedule in schedules]

    answer = 0
    for i in range(len(timelogs)):
        time = timelogs[i]
        # 주말(토요일: 6, 일요일: 0)을 제외한 평일 근무시간만 필터링
        filtered_time = [
            x for idx, x in enumerate(time) 
            if (idx + startday) % 7 not in [0, 6]
        ]

        # 모든 시간 로그가 스케줄보다 작거나 같으면 OK
        if all(j <= schedules[i] for j in filtered_time):
            answer += 1

    return answer

# 문제10. 공원 산책(Lv.1)

def solution(park, routes):
    size = [len(park) - 1, len(park[0]) - 1]
    gate = []

    # 시작 위치(S)와 장애물(X) 찾기
    for row_index, row in enumerate(park):
        if "S" in row:
            position = [row_index, row.index("S")]
        for col_index, char in enumerate(row):
            if char == "X":
                gate.append([row_index, col_index])

    # 방향 이동 처리
    direction = {
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0)
    }

    for route in routes:
        d, n = route.split()
        dx, dy = direction[d]
        n = int(n)

        new_x, new_y = position
        valid = True

        # 이동할 수 있는지 한 칸씩 확인
        for _ in range(n):
            new_x += dx
            new_y += dy

            if new_x < 0 or new_x > size[0] or new_y < 0 or new_y > size[1] or [new_x, new_y] in gate:
                valid = False
                break

        if valid:
            position = [new_x, new_y]

    return position