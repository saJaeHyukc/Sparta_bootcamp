cnt = 1
while True:
    n = input()
    try:
        if n == "exit": break
        elif cnt >= 5:
            n = int(n)
            n *= 2
            print(n)
            break
        
        n = int(n)
        n *= 2
        cnt +=1
        print(n)
        
    except ValueError:
        print(f"입력한 문자는 {n} 입니다.")
        