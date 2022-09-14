number = "num"
#if문을 대신해서 많이 쓰게 됨

try: # try 구문 안에서 에러가 발생할 경우 except로 넘어감
    number = int(number) #"num"을 숫자로 바꾸는 과정에서 에러 발생
except: #에러가 발생했을 때 처리
    print(f"{number}은(는) 숫자가 아닙니다.")
    #pass도 많이 쓴다. continue는 반복문에서 다음 반복문으로 넘어가라는 뜻이므로 pass와 다르다