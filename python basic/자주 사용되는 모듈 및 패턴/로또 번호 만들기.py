import random
from pprint import pprint

def lotto_number_generator(count): #로또 번호 생성기라는 함수 count라는 것을 받아온다
    result = [] #로또 번호를 리스트 형태로 받아온다
    if count < 1: #만약??? count에 0이 되면 값을 써주라고 return으로 false 반환한다
        print("1 이상의 값을 입력해 주세요")
        return False
    
    for _ in range(count): #로또 몇장을 뽑을지 count로 반복문을 돌린다!. 돌려돌려~~
        lotto_numbers = set() #SET으로 중복 값을 없애준다. 로또는 중복이 없으니까
        
        while len(lotto_numbers) < 8: #중복처리가 되었던 것들은 다시 실행해서 while로 조건이 만족할 때까지 랜덤으로 번호를 뽑아온다
            lotto_numbers.add(random.randint(1, 45)) #로또 번호를 추가한다!
            
        result.append(lotto_numbers) #그 로또 번호가 저장된 값들을 이제 붙여준다! result라는 리스트에 복권 번호 8개를!!
        
    return result #저장된 result값을 이제 return으로 반환해준다!!!
lotto_numbers = lotto_number_generator(10)
pprint(lotto_numbers)