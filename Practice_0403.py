'''
문제1. 멀리 뛰기(Lv.1)
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.
'''

'''
n = 1 > 1
n = 2 > 2
n = 3 > 3
n = 4 > 5
n = 5 > 

피보나치 수열을 활용할 수 있을 듯함
'''

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else: 
        return (solution(n-1) + solution(n-2))%1234567

# 위 코드는 시간 복잡도가 너무 높음. 아래는 최적화 코드드

def solution(n):
    a,b = 1, 2
    for _ in range(n-1):
        a,b = b,(a+b) % 1234567
    return a

'''
문제2. N개의 최소공배수(Lv.1)
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
'''

import math

def solution(arr):
    return math.lcm(*arr) # *list: 언패킹

# 다른 풀이. 위 풀이는 프로그래머스 상에서 런타임 에러가 발생생

from math import gcd
from functools import reduce

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    return reduce(lcm, arr)
# reduce 는 리스트의 모든 요소를 하나의 값으로 줄이는 역할
# reduce(함수, 리스트) 로 주어지면 리스트의 가장 첫번째 원소부터 순서대로 함수를 적용
# reduce(add, [1, 2, 3, 4, 5])  # (((1+2)+3)+4)+5
 
'''
문제3. 영어 끝말잇기(Lv.1)
'''

def solution(n, words):
    used_words = set()  # 중복 단어를 확인할 집합
    
    for i in range(len(words)):
        if (i > 0 and words[i-1][-1] != words[i][0]) or words[i] in used_words:
            return [(i % n) + 1, (i // n) + 1]  # 사람 번호, 차례
        
        used_words.add(words[i])  # 단어 저장
        
    return [0, 0]  # 끝까지 규칙을 어기지 않으면 [0,0] 반환

'''
문제4. 예상 대진표(Lv.1)
'''

from math import ceil

def solution(n, a, b):
    a,b = sorted([a,b])
    answer = 1 

    while True:
        if ceil(a/2) == ceil(b/2):
            return answer
        
        a,b = ceil(a/2), ceil(b/2)
        answer += 1

# 다른 풀이. 위 아이디어의 최적화화

def solution(n, a, b):
    rounds = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        rounds += 1
    return rounds

# 다른 풀이.

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

# ^: XOR 연산 => a^b a 와 b 를 비교하여 서로 다른 bit를 1로 저장
# bit_length()를 라운드 수로 생각하여 적용

print("7".bit_length())