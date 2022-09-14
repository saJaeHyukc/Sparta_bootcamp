#filter 함수는 map과 유사한 구조를 가지고 있으며, 조건이 참인 경우 저장한다.
numbers = [1,2,3,4,5,6,7,8]

even_numbers = list(filter(lambda x :x%2 == 0, numbers))
print(even_numbers) #[2,4,6,8]

#filter 함수 또한 list축약식으로 동일한 기능을 구현할 수 있다.
numbers = [1,2,3,4,5,6,7,8]
even_numbers = [x for x in numbers if x%2==0]
print(even_numbers) #[2,4,6,8]

#list 축약식으로 이렇게 표현할 수도 있다!
people = [
    ("lee", 32),
    ("kim", 23),
    ("park", 27),
    ("hong", 29),
    ("kang", 26)
]
people = [x for x in people if x[1] >= 30]
print(people)