'''
문제1. 약수 구하기
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(n):
    answer = []
    for i in range(1,int(n**(0.5))+1):
        if n%i == 0:
            answer.extend([i,n//i])

    return sorted(list(set(answer)))

'''
문제2. 가장 큰 수 찾기
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(array):
    return [max(array), array.index(max(array))]


'''
문제3. 문자열 계산하기
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''



'''
문제4. 문자열 정렬하기
영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

'''
문제5. 숫자 찾기
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
'''

'''
문제6. A로 B 만들기
문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
'''

'''
문제7. k의 개수
1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.
'''

'''
문제8. 숨어있는 숫자의 덧셈셈
문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''

'''
문제9. 7의 개수
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
'''

'''
문제10. 잘라서 배열로 저장하기
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_str, n):
    answer = [my_str[i*n:(i+1)*n] for i in range(len(my_str)//n)]
    a=[1,2,3]

    if "".join(answer) != my_str:
        answer.append(my_str.replace("".join(answer),""))

    return answer

print(solution('abc1Addfggg4556b',6))

# 다른 사람 풀이. 본래 아이디어의 간략화

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]