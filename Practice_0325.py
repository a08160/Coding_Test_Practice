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
문제3. 잘라서 배열로 저장하기
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