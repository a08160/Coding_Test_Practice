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
    answer = money-price*sum(range(1,count+1))
    return answer if answer < 0 else 0

print(solution(3,20,4))