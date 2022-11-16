#replace
def solution(s):
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]
    for i in range(len(a)):
        s = s.replace(a[i], str(i)) #replace는 왼쪽것을 오른쪽으로 바꾼다.
    return int(s)

#####해설#####
arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
arr = 'zeroonehello'
inarr = 'zero' in arr #True 문자열 안에 있는 특정 문자열이 있는지를 판단하기
print(inarr)

######
arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for str in arr:
    print(str)
    
