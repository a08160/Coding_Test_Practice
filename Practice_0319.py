'''
문제1
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(cipher, code):
    code_list = list(filter(lambda x: (x[0] + 1) % code == 0, enumerate(cipher)))
    return "".join([x[1] for x in code_list])

# 다른 풀이. index 활용

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer


'''
문제2.
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요
'''
import math

def solution(array, n):
    lst = [abs(i-n) for i in array]
    min_num = min(lst)
    index_lst = []
    for index, value in enumerate(lst):
        if value == min_num:
            index_lst.append(index)
    
    new_lst = [array[i] for i in index_lst]

    return min(new_lst)

'''
다른 풀이
1. a,n 을 입력받음
2. lamda x: (abs(x-n), x) 의 의미
    : abs(x-n) 거리 기반 정렬
    : x 거리가 같을 경우 값 기준 오름차순 정렬
3. [0]: 가장 작은 값을 반환
'''
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

'''
문제3
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
'''

def solution(numbers):
    num_list = {"zero":0, 
                "one":1, 
                "two":2, 
                "three":3,
                 "four":4, 
                 "five":5, 
                 "six":6, 
                 "seven":7, 
                 "eight":8, 
                 "nine":9}

    for word, num in num_list.items():
        numbers = numbers.replace(word,str(num))

    return int(numbers)

print(solution("onefourzerosixseven"))

# 다른 풀이. 위치 데이터 활용

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)