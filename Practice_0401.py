'''
문제1. 자릿수 더하기(Lv.1)
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
'''

def solution(n):
    return sum(list(map(int,str(n))))

# map을 적용하면 문자열 역시 iterable 한 객체이기 때문에 한 글자씩 함수를 적용함

'''
문제2. 자연수 뒤집어 배열로 만들기(Lv.1)
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
'''

def solution(n):
    return list(map(int,str(n)[::-1]))

'''
문제3. 짝수와 홀수(Lv.1)
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
'''

def solution(num):
    return "Odd" if num%2 != 0 else "Even"

'''
문제4. 평균 구하기(Lv.1)
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
'''

def solution(arr):
    try:
        return sum(arr)/len(arr)
    except:
        pass

'''
문제5. x만큼 간격이 있는 n개의 숫자(Lv.1)
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
'''

def solution(x,n):
    return list(range(x,x*n+1,x)) if x>=0 else list(range(x,x*n-1,x))

# 다른 사람 풀이

def number_generator(x, n):
    return [i * x + x for i in range(n)]

'''
문제6. 나머지가 1이 되는 수 찾기
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
'''

def solution(n):
    if num == 1:
        return 2

    num = n-1
    lst = []
    for i in range(1,int(num//2)+1):
        if num%i == 0:
            lst.extend([i, num//i])

    lst.sort()

    for i in lst:
        if n%i != 0:
            return i

# 다른 사람 풀이
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]

'''
문제7. 두 정수 사이의 합
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''

def solution(a,b):
    a, b = sorted([a, b])
    return sum(range(a,b+1))

'''
문제8. 문자열 내 p와 y의 개수(Lv.1)
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
'''

def solution(s):
    s = s.lower()
    return s.count("p") == s.count("y")

'''
문제9. 정수 내림차순으로 배치하기(Lv.1)
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
'''

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))

'''
문제10. 정수 제곱근 판별(Lv.1)
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.
'''

def solution(n):
    num = n**0.5
    return int((num+1)**2) if int(num) == num else -1

'''
문제11. 최댓값과 최솟값(Lv.2)
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
'''

def solution(s):
    lst = list(map(int, s.split(" ")))
    return f"{min(lst)} {max(lst)}"

'''
문제12. 올바른 괄호(Lv.2)
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
'''

def solution(s):
    while "()" in s:
        s = s.replace("()", "")
    
    return s==""

# 보다 효율적인 코드. 문자열을 지속적으로 복사하지 않기 때문에 공간효율성이 높음

def solution(s):
    stack = []
    for char in s:
        if char == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(char)
    return not stack

'''
문제13. 최솟값 만들기(Lv.2)
길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
즉, 이 경우가 최소가 되므로 29를 return 합니다.

배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

제한사항
배열 A, B의 크기 : 1,000 이하의 자연수
배열 A, B의 원소의 크기 : 1,000 이하의 자연수
'''

def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    
    return answer

# 다른 사람 풀이1. zip 함수를 활용해서 새로운 리스트를 생성
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

# 다른 사람 풀이2. map 활용
def getMinSum(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))

'''
문제14. JadenCase 문자열 만들기(Lv.2)

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.
'''
def solution(s):
    lst = s.split(" ")
    # 각 단어를 소문자로 바꾼 후, 첫 글자만 대문자로 바꿈
    lst = [word.lower().capitalize() for word in lst]
    
    return " ".join(lst)

# 다른 사람 풀이. title(): 문자별 시작값 대문자화
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()

def Jaden_Case(s):
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
    return " ".join(answer)

'''
문제15. 이진 변환 반복하기(Lv.2)
0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

x의 모든 0을 제거합니다.
x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.
'''

def solution(s):
    answer = 0
    time = 0
    while s != "1":
        answer += s.count("0")
        time += 1
        s = s.replace("0","")
        s = str(bin(len(s)))[2:]

    return [time, answer]

'''
문제16. 숫자의 표현(Lv.2)
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
'''

def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i == 0])


'''
문제17. 다음 큰 숫자(Lv.2)
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항
n은 1,000,000 이하의 자연수 입니다.
'''

import numpy as np

def solution(n):
    cnt = bin(n).count('1')  # 현재 숫자의 1의 개수
    
    while True:
        n += 1  # 다음 숫자로 이동
        if bin(n).count('1') == cnt:  # 1의 개수가 동일한 경우
            return n  # 해당 숫자를 반환

'''
문제18. 다음 큰 숫자(Lv.2)
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
'''

# 재귀 함수 활용

def solution(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 1234567)
    return fib[n]

'''
문제19. 정수 삼각형(Lv.3)
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
'''

# 동적 계획법(Dynamic Programming)

def solution(triangle):
    # 삼각형의 마지막 행부터 시작해서, 그 위로 올라가면서 최댓값을 갱신
    for i in range(len(triangle) - 2, -1, -1):  # 마지막 행에서 두 번째 행부터 시작
        for j in range(len(triangle[i])):
            # 현재 위치에서 아래로 갈 수 있는 두 값 중 큰 값을 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # 최종적으로 삼각형의 꼭대기 값이 최댓값
    return triangle[0][0]

'''
문제20. 하샤드 수(Lv.1)
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
'''

def solution(x):
    return x%sum(map(int,list(str(x))))==0

'''
문제21. 음양 더하기(Lv.1)
어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
'''

def solution(absolutes, signs):
    answer = 0 
    for i in range(len(absolutes)):
        answer = answer + absolutes[i] if signs[i] == 1 else answer - absolutes[i]
    
    return answer

'''
문제22. 없는 숫자 더하기(Lv.1)
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    return sum(range(10))-sum(numbers)

'''
문제23. 나누어 떨어지는 숫자 배열(Lv.1)
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
'''

def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

'''
문제24. 서울에서 김서방 찾기(Lv.1)
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
'''

def solution(seoul):
    position = seoul.index("Kim")
    return f"김서방은 {position}에 있다"

'''
문제25. 콜라츠 추측(Lv.1)
1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
'''

def solution(num):

    answer = 0

    while num != 1:
        if num == 626331 or cnt == 500:
            return -1
        if num%2 == 0:
            num /= 2
            answer += 1
        else:
            num = num*3+1
            answer += 1
        cnt+=1

    return answer