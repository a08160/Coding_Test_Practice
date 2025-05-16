'''
velog.io/@leehyuna/코테에-필요한-Python-라이브러리-정리

python 자체의 표준 라이브러리는 허용

import sys
import math
import heapq
import collections
import itertools

외부 라이브러리는 대부분 사용 불가

import numpy
import pandas
import scikit-learn
'''

# spilt()은 연속된 공백을 하나의 공백으로 바라 봄

# 문제1. 날짜 비교하기
# date1/date2 : 연월일 순서로 구성된 리스트임을 가정

def solution(date1, date2):
    return int(date1 < date2)

# 리스트 간 비교. 리스트1 < 리스트2 로 놓게 되면 각 인덱스 별로 순서대로 비교
# 만약 < 의 부등호를 만족하는 관계가 있다면 True를 반환. 하지만 모두 만족하지 않는다면 False를 반환