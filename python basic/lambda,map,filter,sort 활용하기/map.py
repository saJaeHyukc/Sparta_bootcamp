#map은 함수와 리스트르 인자로 받아 리스트의 요소들로 함수를 호출해준다
string_numbers = ["1", "2", "3"]
integer_numbers = list(map(int, string_numbers))
print(integer_numbers) # [1,2,3]

#map 함수를 사용하지 않는 경우 아래와 같이 구현할 수 있다
string_numbers = ["1", "2", "3"]
integer_numbers = []

for i in string_numbers:
    integer_numbers.append(int(i))
    
print(integer_numbers) # [1,2,3]

#list 축약식으로도 동일한 기능을 구현할 수 있다.
#map과 list축약식 중 어떤걸 써야 할지 고민된다면 
string_numbers = ["1", "2", "3"]
integer_numbers = [int(x) for x in string_numbers]
print(integer_numbers) # [1,2,3]

#map 함수와 lambda함수를 함께 사용하면 더 다채로운 기능을 구현할 수 있다.
numbers = [1,2,3,4]
double_numbers = list(map(lambda x:x*2, numbers))
# double_numbers = [x*2 for x in numbers] # list축약식을 사용했을 때의 코드 위와 같은 코드
print(double_numbers) #[2,4,6,8]

