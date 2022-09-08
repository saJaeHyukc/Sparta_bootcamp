import random #숫자 랜덤을 뽑기 위해서!
from datetime import datetime #시간을 표시하기 위해서!
import time #코드 시간길이를 확인하기 위해서!

#1. 숫자를 몇자리로 할 것인지 받기 (ㅇ)
#2. 첫 번째 입력을 받은 수 만큼 중복없는 랜덤한 수 생성 (ㅇ)
#3. 사용자가 숫자를 입력했을 때 규칙에 맞게 ball / out count를 출력 (ㅇ)
#4. 사용자가 정답을 맞춘 경우 아래 항목들을 출력  
#(사용자가 정답을 맞추기까지 입력한 횟수) (ㅇ)
#(사용자가 게임을 시작해서 정답을 맞추기까지 소요된시간) (ㅇ)
#(정답을 맞춘 시점의 날짜/시간) (ㅇ)
#8. 게임을 진행하던 도중, exit을 입력할 경우 프로그램을 종료 (ㅇ)

#1번
start_time = time.time()
a = int(input("몇자리(최대 10자리)로 하시겠습니까?: ")) 
while True:
    if a > 10:
        print("최대 10자리 입니다. 다시 설정해주세요")
        a = int(input())
    else:
        print("게임을 시작합니다!")
        break

#2번
random_number= []
for i in range(1, a+1):
    random_number.append(str(random.randrange(1, 9)))
print(random_number)

#3번
cnt_out = 0 #도전횟수/아웃
cnt_out_max =3  #최대 도전횟수/아웃
cnt_enter = 0

exit = input("게임을 종료하실려면 exit를 입력해주세요. 게임을 시작하시려면 아무키나 눌러주세요.:")
while True:  
    if exit == "exit":
        break
    else:
        if cnt_out>cnt_out_max:
            print(f'패배했습니다. 아웃/도전횟수:{cnt_out}')
            break
        user_number = list(input("자릿 수에 맞게 공백을 추가하여 원하는 숫자를 입력해주세요: ").split())
        print(user_number)
        cnt_enter += 1
    
        cnt_strike = 0
        cnt_ball = 0
        #random_number[4,3,2] user[2,3,4] 
        for i, user in enumerate(user_number): 
            if user == random_number[i]:
                cnt_strike+=1    
            elif user in random_number: #숫자는 맞고 위치가 틀린 것 #random_number[4,2,3] user[2,3,4] 
                #random_number 있는 값을 user에 있는 값을 비교하여 있으면 true 없으면 false 빠져나감
                cnt_ball+=1
                #4번           
        if cnt_strike == 3:
            print(f'승리했습니다. 아웃/도전횟수:{cnt_out},입력한 횟수{cnt_enter}\n' )
            print("정답을 맞춘 시간: ", end="")
            print(datetime.now())
            end_time = time.time()
            print(f"\n정답을 맞추는데 걸린 시간 : {end_time-start_time:}") 
            
        
        elif cnt_strike != 0 or cnt_ball != 0:
            print(f"스트라이크:{cnt_strike}, 볼:{cnt_ball}, 입력한 횟수{cnt_enter}")
            
        else:
            cnt_out += 1
            print("아웃!")
        
        print(f"아웃 카운트:{cnt_out}")



        

    

