from calculator import calculator_funtion       
    
num1, num2 = map(int, input('숫자 두 개를 입력해주세요: ').split()) #num1, num2에 해당하는 값을 int로 입력 받는다
operator = input('연산자를 입력해주세요(*, /, +, -): ')#operator를 string으로 입력받는다

calculator_funtion(num1, num2, operator)
