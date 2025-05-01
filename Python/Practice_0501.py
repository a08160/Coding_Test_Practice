# 문제1. 공백으로 구분하기 1
def solution(my_string):
    return my_string.split()

# 문제2. 공백으로 구분하기 2
def solution(my_string):
    return my_string.strip().split()

# 문제3. ad 제거하기
def solution(strArr):
    return list(filter(lambda x : "ad" not in x, strArr))

# 문제4. 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    return [value.lower() if idx%2 == 0 else value.upper() for idx, value in enumerate(strArr)]

# 문제5. 소문자로 바꾸기
def solution(myString):
    return myString.lower()

# 문제6. 원하는 문자열 찾기
def solution(myString, pat):
    return int(pat.lower() in myString.lower())

# 문제7. 길이에 따른 연산
import numpy as np

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else np.prod(np.array(num_list))

print(solution([2, 3, 4, 5])) # 55

# 문제8. 조건에 맞게 수열 변환하기 1

# 문제9. n보다 커질 때까지 더하기
def solution(numbers, n):
    i = 0
    answer = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    
    return answer

# 다른 풀이
# next(iteratable 객체, default value): next를 사용할 때마다 순서대로 다음 객체를 반환
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)

# 문제10. 할 일 목록
def solution(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]