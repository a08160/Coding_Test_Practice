# 문제1. 공백으로 구분하기 1


# 문제2. 공백으로 구분하기 2


# 문제3. ad 제거하기


# 문제4. 배열에서 문자열 대소문자 변환하기

# 문제5. 소문자로 바꾸기

# 문제6. 원하는 문자열 찾기

# 문제7. 길이에 따른 연산


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