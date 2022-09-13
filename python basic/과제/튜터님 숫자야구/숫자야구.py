import random
import time
import datetime
# length = random.randrange(0, 10) #개발완료 후 사용자가 input으로 변경 예정 #사용자 입력값을 랜덤으로 바꾸는 생각은 못했다.
# length = 5

#과제의 1번!
# Case 1
""" #쌍따옴표 3개를 쓰면 주석처리 된다!
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(number_list)

random_numbers = number_list[0:length]
print(random_numbers)
"""

#Case 2 (pop을 이용)
"""
number_list = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random_numbers = []

for _ in range(length):
    random_numbers.append(number_list.pop(random.randrange(0, len(number_list)))) # 고정 값으로 9를 주면 범위를 벗어나 에러가 나온다

print(number_list)
print(random_numbers)
"""

#Case 3 
def main(): #함수를 쓰면 더 관리하기 편하다
    length = int(input("자릿수를 입력해주세요: "))
    random_numbers = set() # 순서라는 것이 없다! 작은 숫자는 정렬이 되긴하지만 큰 숫자일 경우 정렬이 안됨
    
    while len(random_numbers) < length:
        random_numbers.add(random.randint(0,9))
        
    random_numbers = list(random_numbers)
    random.shuffle(random_numbers)
    print(random_numbers)

    start_time = time.time()
    try_count = 0
    while True:
        input_number = input("값을 입력해주세요 (종료 - exit):")
        if input_number =='exit':
            return
        try_count += 1
        out_count = 0
        ball_count = 0
        strike_count = 0

        for i, v in enumerate(input_number):
            v = int(v)
            if v not in random_numbers: # 포함이 돼있지 않은 경우
                out_count += 1
            else: # 포함이 돼 있는 경우
                if random_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count +=1
        if strike_count == length:
            print("#######################")
            print("정답입니다!")
            print(f'소요시간:{time.time() - start_time:.2f}')
            print(f'클리어시간:{datetime.now()}')
            print(f'도전횟수:{try_count}')
            print("#######################")
            return
        print(f'{ball_count}볼 {strike_count}스트라이크 {out_count}아웃')

main()