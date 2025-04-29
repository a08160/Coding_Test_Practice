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

# 문제4. 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num]*num)
    return answer

# 문제5. rny_string
def solution(rny_string):
    return rny_string.replace("m","rn")

# 문제6. x 사이의 개수
def solution(myString):
    return list(len(str1) for str1 in myString.split("x"))

print(solution("oxooxoxxox"))