def solution(left, right):
    answer = 0
    return answer



######해설#####
cnt = 0
a = 4
for i in range(1, a+1):
    if a % i == 0:
        cnt +=1
if cnt % 2 == 0:
    print("약수 갯수 짝")
else:
    print("약수 갯수 홀")
    
