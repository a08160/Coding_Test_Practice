# 문제1. A 강조하기

def solution(myString):
    myString = myString.lower()
    return myString.replace("a","A")

# 문제2. 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)

# 문제3. 문자열 정수의 합
def solution(num_str):
    return sum(map(int, num_str))

# 문제4. 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num]*num)
    return answer

# 문제5. rny_string
def solution(rny_string):
    return rny_string.replace("m","rn")

# 문제6. x 사이의 개수
def solution(myString):
    return list(len(str1) for str1 in myString.split("x"))

# 문제7. 정수를 나선형으로 배치하기
'''
배열을 완전히 list로 바꾸기
list(array): 첫번째 축을 기준으로 list로 변환하기 때문에 내부는 여전히 array로 남아있음
따라서 tolist()를 사용하여 완전히 list로 변환해야 함
'''
def solution(n):
    board = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]
    
    x = y = 0
    dir = 0  # 시작 방향: 오른쪽
    for i in range(1, n*n + 1):
        board[x][y] = i
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            x, y = nx, ny
        else:
            dir = (dir + 1) % 4  # 방향 전환
            x += dx[dir]
            y += dy[dir]
    return board
