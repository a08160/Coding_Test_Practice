# 문제1. 1로 만들기

def solution(num_list):
    answer = 0
    multiple_2 = [2,4,8,16]
    
    for num in num_list:
        # num보다 큰 multiple_2 원소의 개수를 센다
        count = sum(1 for x in multiple_2 if num >= x)
        answer += count
    
    return answer

'''
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)
'''