import random
print("가위, 바위, 보를 시작합니다!")


while True:
    my_list = ['가위', '바위', '보']
    my_select = random.choice(my_list)
    u = input("가위, 바위, 보 중 입력해주세요")
    if u == "가위" or u == "바위" or u == "보":
        if my_select == u: print("게임에서 승리하셨습니다!")
        else:
            print("게임에서 지셨군요? ")
            print(f"컴퓨터는 {my_select}입니다!")
            game_over = input("게임을 종료하시려면 exit을 입력해주세요. 계속하시려면 아무것이나 입력해주세요.")
            if game_over == "exit":
                print("게임이 종료되었습니다.") 
                break
            else:
                print("게임이 시작됩니다!")
                continue
    else:
        print("다시 입력해주세요")