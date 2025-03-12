# 코딩테스트 입문

'''
문제1 설명. 대소문자 변경
문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
'''
# 내 풀이
# 대문자와 소문자 간의 ASCII코드 값이 32 만큼 차이 나는 것을 반영하여 아스키코드로 변형 후 대소문자의 형태에 따라 32를 더하거나 뺀 후 다시 유니 코드로 변형

def solution(my_string):
    ascii_lst = [ord(alp) for alp in my_string]
    uni_lst = []
    for alp in ascii_lst:
        if alp < 97:
            uni_lst.append(chr(alp+32))
        else:
            uni_lst.append(chr(alp-32))
    return "".join(uni_lst)

# 다른 풀이

# swapcase() 는 대소문자를 변형하는 함수
def solution(my_string):
    return my_string.swapcase() 

# lower 과 upper 을 활용해서 대소문자 변형
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer

'''
문제2. 인덱스 바꾸기기
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

'''
틀린 풀이
def solution(my_string, num1, num2):
    my_string[num1],my_string[num2] = my_string[num2], my_string[num1]
    return my_string

이유. 문자열(str)은 불변(immutable) 객체이기 때문에 직접 인덱스를 수정할 수 없음음
'''

def solution(my_string, num1, num2):
    lst = list(my_string)
    lst[num1],lst[num2] = lst[num2], lst[num1]
    return "".join(lst)