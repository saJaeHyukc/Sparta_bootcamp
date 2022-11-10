def solution(n):
    answer = []
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer

print(solution(123456))