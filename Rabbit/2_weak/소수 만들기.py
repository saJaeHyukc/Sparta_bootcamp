from itertools import combinations

def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, num-1):
            if num % n == 0:
                return False        
        return True

def solution(nums):
    answer = 0
    c = list(combinations(nums, 3))
    for i in range(len(c)):
        if is_prime_number(sum(c[i]))==True:
            answer += 1 
    return answer

#고민하기
#조합을 사용(그 세자리 수의 변수 생각)
#그 값이 소수인지 판단

#더 알게된 점
#combinations를 사용할 수 있다는 것
#함수를 두개를 써도 된다는 것