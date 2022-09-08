import random

STRING= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789" #이 중에 바꿀 비밀번호를 랜덤으로 생성

def password_generator(length): # length를 넣어 몇자리를 설정할지 정한다 
    password = "" # string으로 값을 password에 넣을 변수를 만든다
    for _ in range(length): # 길이 만큼 돌린다
        password += STRING[random.randrange(0, len(STRING))] #string에 있는 0번째부터 랜덤으로 길이까지 돌려 pasword값에 저장한다
        
    return password # return으로 저장한 패스워드 반환(들여쓰기 잘하기!!!!)

def main():
    length = int(input("비밀번호 길이를 입력해주세요!:")) #main으로 입력받아 인풋값을 받는다 그것을 정수로 바꾸고
    password = password_generator(length) #비밀번호 랜덤 함수로 이동하여 길이만큼 저장한다음
    print(password) # 비밀번호를 출력한다
    
main()