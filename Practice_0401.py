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
'''