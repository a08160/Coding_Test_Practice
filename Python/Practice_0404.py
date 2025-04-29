'''
문제1. 예산(Lv.1)
'''

def solution(d, budget):
    d.sort()
    lst = [sum(d[0:i]) for i in range(1, len(d)+1)]

    lst = [ i <= budget for i in lst]

    return sum(lst)

'''
문제2. 3진법 뒤집기(Lv.1)
'''

def solution(n):
    lst = []

    # Convert decimal to reversed ternary
    while n > 0:
        lst.append(str(n % 3))
        n //= 3

    # Convert reversed ternary back to decimal
    return int(''.join(lst), 3)


'''
문제3. 크기가 작은 부분문자열(Lv.1)
'''

def solution(t,p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1

    return answer

'''
문제4. 삼총사(Lv.1)

재귀 함수 활용
'''

def solution(number):
    def triplets(idx, selected):
        # 3명을 선택한 경우 합이 0인지 확인
        if len(selected) == 3:
            return 1 if sum(selected) == 0 else 0

        # 배열의 끝까지 탐색한 경우 종료
        if idx >= len(number):
            return 0

        # 현재 숫자를 선택하는 경우와 선택하지 않는 경우로 나누어 재귀 호출
        return triplets(idx + 1, selected + [number[idx]]) + triplets(idx + 1, selected)

    return triplets(0, [])

# 다른 풀이

from itertools import combinations

def solution(number):
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt

'''
문제5. 이상한 문자 만들기(Lv.1)
'''

def solution(s):
    lst = s.split(" ")
    lst2 = []

    for i in lst:
        lst2.append(''.join(value.upper() 
                            if index % 2 == 0 
                            else value.lower() 
                            for index, value in enumerate(i)))

    return " ".join(lst2)

print(solution("t"))

'''
문제6. 괄호 회전하기(Lv.2)
'''

def is_valid(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():  # 여는 괄호
            stack.append(char)
        elif char in bracket_map.keys():  # 닫는 괄호
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return not stack  # 스택이 비어 있으면 올바른 괄호 문자열

def solution(s):
    count = 0
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]  # 문자열 왼쪽으로 회전
        if is_valid(rotated_s):
            count += 1
    
    return count

'''
문제7. 행렬의 곱셈(Lv.2)
'''

def solution(arr1, arr2):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*arr2)] for row in arr1]

