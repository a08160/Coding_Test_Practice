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