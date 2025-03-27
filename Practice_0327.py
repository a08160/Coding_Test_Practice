'''
문제1.
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
'''

# 풀이. int(문자, 진법) => 문자를 진법에 해당하는 수로 인식하고 10진수로 변환

def solution(bin1, bin2):
    return str(bin(int(bin1,2)+int(bin2,2)))[2:]

'''
문제2.
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.
'''

def solution(sides):
    return len(list(range(max(sides)-min(sides),sum(sides))))-1

# 다른 사람 풀이.

def solution(sides):
    return 2 * min(sides) - 1

'''
문제3.
머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
'''

def solution(keyinput, board):
    x, y = 0, 0
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    for key in keyinput:
        if key == "up" and y < y_limit:
            y += 1
        if key == "down" and y > -y_limit:
            y -= 1
        if key == "left" and x > -x_limit:
            x -= 1
        if key == "right" and x < x_limit:
            x += 1
    
    return [x, y]

'''
문제4.
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(quiz):
    answer = []
    for q in quiz:
        expression, result = q.split(' = ')
        if eval(expression) == int(result):
            answer.append('O')
        else:
            answer.append('X')
    return answer

# 다른 사람 풀이. eval 활용

def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]    

'''
문제5.
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
'''

def solution(spell, dic):
    spell_set = set(spell)

    for word in dic:
        if set(word) == spell_set and len(word) == len(spell):
            return 1
    return 2

'''
문제6.
머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
'''

def solution(M, N):
    return M*N-1

'''
문제7.
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
'''

def solution(dots):
    lst = []
    for i in dots:
        for j in dots:
            lst.append(((i[0]-j[0])**2+(i[1]-j[1])**2)**0.5)
    new_lst = sorted(set(lst))
    if len(new_lst) == 3:
        return int(new_lst[1]**2)
    
    return int(new_lst[1]*new_lst[2])

'''
문제8. 로그인 성공?
머쓱이는 프로그래머스에 로그인하려고 합니다. 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.
'''

def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for id, pw in db:
        if id_pw[0] == id:
            return "wrong pw"
    return "fail"

# 다른 사람 풀이. dict.get(key, default=None): 찾고자하는 키의 value를 반환 없다면 default를 반환

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"