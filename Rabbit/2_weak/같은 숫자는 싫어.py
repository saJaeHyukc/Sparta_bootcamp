def solution(arr):
    answer = []
    if arr[0] == arr[1]:
        answer.append(arr[0])
        
    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    if len(answer) > 1:
        if answer[0] == answer[1]:
            del answer[0]
    return answer


#고민하기
#1. 앞 뒤 번호가 같으면 앞 번호를 추가시킴
#2. 앞 뒤 번호가 다르면 그 값을 넣음
#3. 값이 [1, 1]일 경우도 있으니 answer에 범위 지정
#4. 앞 뒤 번호를 참조하는데 중복된 값이 들어갈 수 있으니 그 값을 삭제

#더 알게된 점
#del과 remove가 다르다는 것
#i+1하면 index out of range라는 오류가 뜸
