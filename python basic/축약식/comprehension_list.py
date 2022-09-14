#[list에 담길 값 for 요소 in 리스트]
numbers = [x for x in range(5)] #[0,1,2,3,4]
numbers = [x * 2 for x in range(5)] #0,2,4,6,8]
numbers = [2 for _ in range(5)] #[2,2,2,2,2]
even_numbers = [x for x in range(10) if x % 2 == 0] #[0,2,4,6,8,]

#활용방법은?
people = [
    ("lee", 32),
    ("kim", 23),
    ("park", 27),
    ("hong", 29),
    ("kang", 26)
]

# sum_age = 0
# for i in people:
#     sum_age += i[1]
# avg_age = sum_age / len(people)
# print(avg_age)

avg_age = sum([x[1] for x in people]) / len(people) #x는 튜플이 담기며 x의 1번째 인덱스 즉 나이가 담긴다.
print(avg_age)

# #input을 이용한 것
# count = int(input())
# user_inputs = [input() for x in range(count)]
# print(user_inputs)