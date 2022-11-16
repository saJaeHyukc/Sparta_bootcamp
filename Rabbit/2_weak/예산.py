def solution(d, budget):
    answer = 0
    answer_list = []
    d.sort()
    for i in range(len(d)):
        answer += d[i]    
        if budget >= answer:
            answer_list.append(d[i])
    return len(answer_list)

#고민하기
#1. 먼저 작은 수 부터 넣기(정렬)
#2. answer과 budget을 비교하여 answer_list에 값 넣기