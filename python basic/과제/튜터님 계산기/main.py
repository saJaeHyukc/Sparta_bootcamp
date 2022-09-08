import calc

def main():
    #*을 사용하면??
    #["3", "+", "5"]
    #"3", "+","5"
    try:
        result = calc.calc(*input().split(" ")) #*이라는 것은 리스트를 풀어서 표현한다
        print(result)
    except:
        print("수식을 잘못 입력하셨습니다")
    
main()

#print(eval(input())) 이라는 것도 있는데 보안이 취약해 사용하지말자!