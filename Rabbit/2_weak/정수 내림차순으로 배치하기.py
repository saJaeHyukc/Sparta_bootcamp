def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int("".join(n))

print(solution(12345))

#더 알게된 점
#정렬을 역순으로 하려면 reverse=True를 사용하면 되는것
#리스트를 값으로 변환시키려면 ""을 기준으로 join을 쓸 수 있다는 것