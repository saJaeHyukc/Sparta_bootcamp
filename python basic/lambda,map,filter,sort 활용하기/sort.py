# sort함수를 사용하면 list를 순서대로 정렬할 수 있다
numbers = [5,3,2,4,6,1]
numbers.sort()
print(numbers) # [1,2,3,4,5,6]

# 역순으로도 돌릴 수 있다.
numbers = [5,3,2,4,6,1]
numbers.sort(reverse=True)
print(numbers) # [6,5,4,3,2,1]

#sort와 lambda를 활용한 예제
people = [
    ("lee", 32),
    ("kim", 23),
    ("park", 27),
    ("hong", 29),
    ("kang", 26)
]

#나이 순으로 정렬하기
people.sort(key=lambda x: x[1])#, reverse=True역순 정렬도 가능) #key(어떤 기준으로 정렬할 것인가)라는 옵션에서 lambda를 넣을 수 있다. 
print(people)

#result print
# [('kim', 23), ('kang', 26), ('park', 27), ('hong', 29), ('lee', 32)]

#나이와 이름순으로 정렬하기!
people = [
    ("lee", 32),
    ("lee", 31),
    ("lee", 29),
    ("lee", 19),
    ("kim", 23),
    ("park", 27),
    ("hong", 29),
    ("kang", 26)
]

people.sort(key=lambda x: (x[0],x[1])) #튜플을 감싸서 x[0]을 먼저 나타내주고 그다음 x[1]을 기준으로 나타낸다