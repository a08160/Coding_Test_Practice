'''
문제1. 가운데 글자 가져오기(Lv.1)
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''

def solution(s):
    return s[len(s)//2+(len(s)%2-1):len(s)//2+1]

'''
문제2. 제일 작은 수 제거하기(Lv.1)
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
'''

def solution(arr):
    if len(arr) != 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

'''
문제3. 핸드폰 번호 가리기(Lv.1)
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
'''

def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

'''
문제4. 내적(Lv.1)
길이가 같은 두 1차원 정수 배열 a,b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1]+....+a[n-1]*b[n-1] 입니다(n은 a,b의 길이)
'''

def solution(arr1,arr2):
    return sum([a*b for a,b in zip(arr1,arr2)])

# 다른 풀이. lambda로 함수 정의 하기
solution = lambda x, y: sum(a*b for a, b in zip(x, y))

'''
문제5. 수박수박수박수박수박수?(Lv.1)
길이가 n이고, "수박수박수박수..."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
예를 들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
'''

def solution(n):
    return ("수박"*n)[:n]

'''
문제6. 약수의 개수와 덧셈(Lv.1)
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요
'''
# Point. 제곱수만이 약수의 개수가 무조건 홀수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

'''
문제7. 문자열 내림차순으로 배치하기(Lv.1)
문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬해서 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
'''

def solution(s):
    lst = sorted(list(s), reverse=True)
    return "".join(lst)

'''
문제8. 부족한 금액 계산하기(Lv.1)
새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.
'''

def solution(price,money, count):
    answer = price*sum(range(1,count+1))-money
    return answer if answer > 0 else 0

'''
문제9. 문자열 다루기 기본(Lv.1)
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는 지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
'''

def solution(s):
    return s.isdigit() and len(s) in [4,6]

'''
문제10. 행렬의 덧셈(Lv.1)
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행랠 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
'''

import numpy as np

def solution(arr1, arr2):
    new_arr = np.array(arr1)+np.array(arr2)
    return list(map(list,new_arr))

# 다른 풀이. 재귀 함수 활용

def solution(arr1, arr2):
    if isinstance(arr1, list):  # arr1 이 list 타입인 지를 판별
        return [solution(a1, a2) for a1, a2 in zip(arr1, arr2)]
    else:  # 리스트가 아니라 단일 숫자일 경우, 덧셈 수행
        return arr1 + arr2
    
'''
문제11. 짝지어 제거하기(Lv.2)
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.
'''

def solution(s):
    for _ in range(len(s) // 2):
        for i in set(s):
            s = s.replace(i * 2, "")
    return int(s == "")
            
# 위 코드는 시간 복잡도가 너무 높음
def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return int(not stack)

'''
문제12. 카펫(Lv.2)
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
'''

def solution(brown,yellow):
    column = 1

    while ((brown-4)/2-column)*column != yellow:
        column += 1
    
    return [int(brown/2-column),column+2]

'''
문제13. 점프와 순간 이동(Lv.2)
'''

def solution(N):
    return bin(N).count('1')

'''
문제14. 구명보트(Lv.2)
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

'''
# Greedy method
def solution(people, limit):
    people.sort()  # 몸무게를 오름차순으로 정렬
    left, right = 0, len(people) - 1  # 가장 가벼운 사람과 가장 무거운 사람을 가리키는 포인터
    boats = 0  # 필요한 구명보트 개수
    
    while left <= right:
        if people[left] + people[right] <= limit:  # 두 사람이 함께 탈 수 있는 경우
            left += 1  # 가벼운 사람도 탑승
        right -= 1  # 무거운 사람 탑승
        boats += 1  # 보트 사용 증가
    
    return boats  # 최소 구명보트 개수 반환

# 예제 테스트
print(solution([70, 50, 80, 50], 100))  # 출력: 3

'''
문제15. 귤 고르기(Lv.2)
경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(k, tangerine):
    set1 = set(tangerine)
    dct = {}
    for i in set1:
        dct.update({i:tangerine.count(i)})

    dct = dict(sorted(dct.items(),reverse=True, key = lambda x: x[1]))

    kind = 0

    for value in dct.values():
        k -= value
        kind += 1

        if k <= 0:
            return kind
    
    return kind

# 축약 코드
def solution(k, tangerine):
    dct = {}
    for t in tangerine:
        dct[t] = dct.get(t, 0) + 1  # 딕셔너리에 값 저장

    sorted_values = sorted(dct.values(), reverse=True)  # 값 기준 정렬

    kind = 0
    for value in sorted_values:
        k -= value
        kind += 1
        if k <= 0:
            return kind
    
    return kind