'''
문제1. 문자열 계산하기
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''

def solution(my_string):
    lst = my_string.split(" ")
    lst_sign =[index for index, value in enumerate(lst) if index%2 == 1]
    answer = int(lst[0])
    for sign in lst_sign:
        if lst[sign] == "+":
            answer += int(lst[sign+1])
        else:
            answer -= int(lst[sign+1])
    return answer

# 다른 사람 풀이1. a - b => a + (-b)

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# 다른 사람 풀이2. eval: 문자열로 구성된 파이썬 코드를를 실행시켜줌줌
solution=eval

'''
문제2. 문자열 정렬하기
영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(my_string):
    return ''.join(sorted(my_string.lower()))

'''
문제3. 숫자 찾기
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k))+1
    else:
        return -1

'''
문제4. A로 B 만들기
문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
'''
from collections import Counter

def solution(before, after):
    dict_before = Counter(before)
    dict_after = Counter(after)

    if dict_before == dict_after:
        return 1
    else:
        return 0
    
# 다른 사람 풀이.

def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0

'''
문제5. k의 개수
1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.
'''

def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        answer += str(num).count(str(k))
    return answer

'''
문제6. 숨어있는 숫자의 덧셈
문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    # 숫자가 아닌 문자는 공백으로 치환
    for i in my_string:
        if not i.isdigit():
            my_string = my_string.replace(i, " ")
    
    # 공백 기준으로 split 후 정수로 변환하여 합산
    return sum(map(int, my_string.split()))


print(solution("aAb1B2cC34oOp"))

'''
문제7. 7의 개수
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
'''

def solution(array):
    answer = 0
    for num in array:
        answer += str(num).count("7")
    return answer

# 다른 사람 풀이. 내 풀이의 간략화

def solution(array):
    return str(array).count('7')