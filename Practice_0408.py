# 문제1. 부분 문자열(Lv.1)

def solution(str1, str2):
    return int(str1 in str2)

# 문제2. 숫자 문자열과 영단어(Lv.1)

def solution(s):
    dct ={"zero":"0",
          "one":"1",
          "two":"2",
          "three":"3",
          "four":"4",
          "five":"5",
          "six":"6",
          "seven":"7",
          "eight":"8",
          "nine":"9",
          }
    
    for key, value in dct.items():
        s = s.replace(key,value)
    
    return int(s)

# 문제3. 푸드 파이트 대회(Lv.1)

def solution(food):
    s = ""
    num = 1
    for i in food[1:]:
        s += f"{num}"*(i//2)
        num +=1
    
    return s+"0"+s[::-1]

# 문제4. 콜라 문제(Lv.1)

def solution(a, b, n):
    answer = 0
    while n // a != 0:
        answer += b * (n // a)
        n = b * (n // a) + n % a

    return answer

# 다른 풀이

solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# 문제5. 문자열 내 마음대로 정렬하기(Lv.1)
# 리스트 정렬 활용

# key = 정렬 기준
# x[n] 을 기준으로 먼저 정렬. x[n] 이 같을 경우 x 를 기준으로 정렬렬

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

# 문제6. 명예의 전당(1) (Lv.1)

def solution(k, score):
    lst = []
    answer = []
    
    for s in score:
        lst.append(s)
        lst.sort(reverse=True)
        
        if len(lst) > k:
            lst = lst[:k]
            
        answer.append(min(lst))
    
    return answer

# 문제7. [1차] 비밀지도(Lv.1)

'''
bin_num = bin(arr1[i] | arr2[i])[2:].zfill(n) 설명

1. arr1[i] | arr2[i] 각 자리에 대해서 하나라도 1 이면 1을 반환 
2. bin(arr1[i] | arr2[i])[2:] 이진수 문자열로 변환 후 0b 제거
3. zfill(n) 문자열 길이를 n 으로 맞추되 길이가 짧을 시 앞에 0을 추가해서 길이를 맞춤 
'''

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # OR 연산 후 이진수로 변환 (zfill로 앞자리 0 맞춤)
        bin_num = bin(arr1[i] | arr2[i])[2:].zfill(n)

        # 1이면 '#', 0이면 ' ' 으로 변환
        line = ''.join('#' if ch == '1' else ' ' for ch in bin_num)
        answer.append(line)

    return answer

# 문제8. 카드 뭉치(Lv.1)

def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and cards1[0] == i:
            cards1.pop(0)
        elif cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

# 문제9. 추억 점수(Lv.1)
# get(key, default): 딕셔너리 전용 함수 / 딕셔너리에서 key 값에 해당되는 value 반환 없으면 default 반환환

def solution(name, yearning, photos):
    answer = []
    dct = dict(zip(name, yearning))
    
    for photo in photos:
        score = sum(dct.get(person, 0) for person in photo)
        answer.append(score)
    
    return answer

# 문제10. 폰켓몬(Lv.1)

def solution(nums):
    num = len(nums)//2
    kind = len(set(nums))

    if num <= kind:
        return num
    else:
        return kind
    
# 다른 사람 풀이

def solution(ls):
    return min(len(ls)/2, len(set(ls)))