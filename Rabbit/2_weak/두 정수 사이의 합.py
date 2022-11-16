def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        for i in range(a, b):
            answer += i
    else: 
        for i in range(b, a):
            answer += i
    return answer

#고민하기
#1. a와 b가 같을 때 생각
#2. a가 b보다 클 때 생각
#3. a가 b보다 작을 때 생각

        

