def solution(s):
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]
    for i in range(len(a)):
        s = s.replace(a[i], str(i))
    return int(s)



