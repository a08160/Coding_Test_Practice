'''
문제1. 저주의 숫자 3
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.
'''

def solution(n):
    count = 0
    num = 0
    
    while count < n:
        num += 1
        if num % 3 != 0 and '3' not in str(num):
            count += 1

    return num

'''
문제2. 유한 소수 판별하기기
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
'''
def solution(a,b):
    def divisor(n):
        lst = []
        
        x = 2

        while x <= n:
            if n % x == 0:
                if x not in lst:
                    lst.append(x)
                n //= x
            else:
                x += 1

        return lst
    
    lst_a = divisor(a)
    lst_b = divisor(b)

    print(lst_a)
    print(lst_b)

    lst_prime = list(filter(lambda x : x not in lst_a, lst_b))

    if set(lst_prime).issubset([2,5]): # issubset은 집합 간 포함관계를 확인할 때 활용
        return 1
    else:
        return 2

# 다른 사람 풀이. 1~1000까지라는 점을 활용

def solution(a, b):

    return 1 if a/b * 1000 % 1 == 0 else 2

'''
문제3. 문자열 밀기
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(A, B):
    if A == B:
        return 0
    answer = 0
    A = list(A)
    for _ in range(len(A)):
        wrd = A.pop()
        A.insert(0, wrd)
        answer += 1
        if ''.join(A) == B:
            return answer
    return -1

# 다른 사람 풀이. 개천재인듯

solution=lambda a,b:(b*2).find(a)

'''
문제4. 특이한 정렬
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x - n), -x))

'''
문제5. 다항식 더하기
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.
'''

def solution(polynomial):
    terms = polynomial.split(" + ")  # 항을 "+" 기준으로 분리
    x_coeff = 0  # x의 계수
    constant = 0  # 상수 항
    
    for term in terms:
        if 'x' in term:
            # "x"가 포함된 항 처리
            if term == "x":
                x_coeff += 1  # "x"는 계수 1
            else:
                # x와 숫자가 함께 있는 경우 (예: "2x" 또는 "3x")
                x_coeff += int(term.replace('x', ''))  # 숫자를 추출하여 더함
        else:
            # x가 포함되지 않은 항은 상수 항으로 처리
            constant += int(term)
    
    # 결과 생성
    result = []
    
    # x가 있을 경우 "x" 항 추가
    if x_coeff != 0:
        if x_coeff == 1:
            result.append("x")
        else:
            result.append(f"{x_coeff}x")
    
    # 상수 항이 있을 경우 추가
    if constant != 0:
        result.append(str(constant))
    
    # 결과 반환
    return " + ".join(result)

'''
문제6. 다음에 올 숫자
등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.
'''

def solution(common):
    if common[1]-common[0] == common[2]-common[1]: # 등차
        return common[-1]+common[1]-common[0]
    else: # 등비
        return common[-1]*common[1]//common[0]
    
'''
문제7. 연속된 수의 합
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
'''

def solution(num, total):
    if total%num == 0:
        return list(range(total//num - num//2,total//num + num//2+1))
    else:
        return list(range(total//num - num//2+1,total//num + num//2+1))
    
print(solution(4,14))

'''
문제8. 안전지대
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
'''

def solution(board):
    n = len(board)  # 보드의 크기를 n으로 설정 (정사각형이 아닌 경우를 대비하여 len(board))

    lst = []
    for i, row in enumerate(board):
        for j, target in enumerate(row):
            if target == 1:
                # 지뢰가 있는 위치에서 8방향 + 자기 자신 추가
                lst.extend([
                    [i-1, j-1], [i-1, j], [i-1, j+1],
                    [i, j-1], [i, j], [i, j+1],
                    [i+1, j-1], [i+1, j], [i+1, j+1]
                ])
    
    # 유효한 인덱스만 남기기 (보드 크기 내에서)
    lst = list(filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < n, lst))
    
    # 중복된 좌표를 제거하고, 안전한 칸 수를 계산
    dangerous_count = len(set(map(tuple, lst)))
    
    # 전체 칸 수에서 위험 지역을 제외한 안전 지역의 수를 반환
    return n * n - dangerous_count

'''
문제9. 겹치는 선분의 길이
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.
'''

def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

'''
문제10. 약수의 합
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''

def solution(n):
    total_sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:  # i는 n의 약수
            total_sum += i
            if i != n // i:  # n // i도 약수 (i와 n // i가 다를 때만 더함)
                total_sum += n // i
    return total_sum
