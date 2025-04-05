'''
문제1. 최소직사각형(Lv.1)
'''

def solution(sizes):
    sizes = [sorted(i) for i in sizes]
    lst_hori = sorted([i[0] for i in sizes]) # 가로 길이 정렬
    lst_vert = sorted([i[1] for i in sizes]) # 세로 길이 정렬

    return lst_hori[-1]*lst_vert[-1]

# 코드 간략화

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

'''
문제2. 시저 암호(Lv.1)
'''

def solution(s, n):
    lst = list(s)
    lst_1 = range(65, 91)
    lst_2 = range(97, 123)

    for i in range(len(lst)):
        if lst[i] != " ":
            ascii_value = ord(lst[i])
            if ascii_value in lst_1:
                lst[i] = chr((ascii_value - 65 + n) % 26 + 65)
            elif ascii_value in lst_2:
                lst[i] = chr((ascii_value - 97 + n) % 26 + 97)
    
    return "".join(lst)

print(solution("a B z", 4))

'''
문제3. 가장 가까운 같은 글자(Lv.1)
'''

def solution(s):
    answer = []
    last_seen = {}

    for i, char in enumerate(s):
        if char in last_seen:
            distance = i - last_seen[char]
            answer.append(distance)
        else:
            answer.append(-1)
        last_seen[char] = i  # 현재 문자의 위치를 기록

    return answer

'''
문제4. K번째 수(Lv.1)
'''

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

'''
문제5. 두 개 뽑아서 더하기(Lv.1)
'''

def solution(numbers):
    return sorted(set(i + j for idx, i in enumerate(numbers) for j in numbers[idx+1:]))

print(solution([2,1,3,4,1]))