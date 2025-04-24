# 문제1. A 강조하기

def solution(myString):
    myString = myString.lower()
    return myString.replace("a","A")

# 문제2. 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)

# 문제3. 문자열 정수의 합
def solution(num_str):
    return sum(map(int, num_str))

print(solution("100000"))