import operator

def solution(N, stages):
    answer = []
    dic = {}
    
    for i in range(1, N+1):
        dic[i] = stages.count(i) / len(stages)
        while i in stages:
            stages.remove(i)
            
    a = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    
    for i in range(len(a)):
        answer.append(a[i][0])

    return answer

#고민하기
#1. 실패율을 구함
#2. 실패율을 구한 stages를 삭제
#3. 실패율 값들을 내림차순으로 정렬
#4. 실패율이 높은 순부터 나열

#더 알게된 점
#리스트에 있는 중복 값을 삭제하려면 반복문을 돌릴 수 있는 것
#사전형일 때 정렬할 수 있는 operator라는 모듈을 사용할 수 있는 것