def solution(array, commands):
    answer = []
    temp = []
    
    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        temp = array[i-1:j]
        temp.sort()
        k = commands[a][2]
        answer.append(temp[k-1])
        
    return answer

#고민하기
#1. commands의 i번째와 j번째 k를 구한다.
#2. array를 그에 맞게 뽑아낸다
#3. 정렬시킨다
#4. 인덱싱을 찾는다.
#5. 값을 넣는다