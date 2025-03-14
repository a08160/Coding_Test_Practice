'''
문제1. 문자열 정렬하기
문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.
'''

def solution(my_string):
    lst = list(my_string)
    new_list = []
    for i in lst:
        try:
            new_list.append(int(i))
        except:
            continue

    new_list.sort()

    return new_list

# 다른 풀이. isdigit 활용하기
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))

'''
문제2. 소인수 분해
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    return factors

'''
문제3. 컨트롤 제트
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(s):
    lst1 = s.split()
    result = 0
    for index, value in enumerate(lst1):
        try:
            result += int(value)
        except:
            result -= int(lst1[index-1])
    return result

print(solution("-1 -2 -3 Z"))
# 3 반환 정답: -3
# 이유: isdigit의 양의 정수만 수로 인식하기 때문에, -1,-2,-3 은 숫자로 인식되지 않음

# 다른 풀이
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer

'''
문제4. 중복된 문자 제거거
문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    # 순서 유지하면서 중복 제거
    new_list = list(dict.fromkeys(my_string))
    return "".join(new_list)

# dict.fromkeys("문자열"): 문자열 내 순서대로 key 값을 저장하며 중복값을 제거해서 반영(value는 모두 None 으로 설정)
# list(dict.fromkeys("문자열")): 중복되지 않게 key 값만 list로 저장
# EX. list(dict.fromkeys("multiple")) => [m,u,l,t,i,p,e]