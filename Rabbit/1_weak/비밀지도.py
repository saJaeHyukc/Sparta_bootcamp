def solution(n, arr1, arr2):
    answer = []
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

answer = [''] * n
for i in range(n):
    bin1 = bin(arr1[i])[2:].zfill(n)
    bin2 = bin(arr1[i])[2:].zfill(n)
    for j in range(n):
        if bin1[j] == '0' or bin2[j] == '0':
            answer[i] += ' '
        else:
            answer[i] += '#'

print(answer)


# for i in range(n):
#     answer[i] += bin(arr2[i])[2:].zfill(3)

