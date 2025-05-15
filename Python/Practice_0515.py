# 문제1. 주사위 게임 3

from collections import Counter

def solution(a, b, c, d):
    dct = dict(sorted(Counter([a,b,c,d]).items(), key = lambda x: x[1]))
    size = len(dct)
    lst = list(dct.keys())
    if size == 1:
        return a*1111
    elif size == 4:
        return min([a,b,c,d])
    else:
        if max(dct.values()) == 3:
            return (10*lst[1]+lst[0])**2
        elif min(dct.values()) == 1:
            return lst[0]*lst[1]
        else:
            return (lst[0]+lst[1])*abs(lst[0]-lst[1]) 
        
# 문제2. 원소들의 곱과 합

from math import prod

def solution(num_list):
    return 0 if prod(num_list) > sum(num_list)**2 else 1

'''
from functools import reduce

def solution(num_list):
    total_sum = sum(num_list)
    total_product = reduce(lambda x, y: x * y, num_list)
    return 1 if total_product < total_sum ** 2 else 0
'''