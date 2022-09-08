def calculator_funtion(num1, num2, operator):
    if operator == '*':#operator 값이 * 일경우 num1, num2를 곱한다
        print(num1 * num2)
    elif operator == '/':#operator 값이 / 일경우 num1, num2를 나눈다
        print(num1 / num2)
    elif operator == '+': #operator 값이 + 일경우 num1, num2를 더한다
        print(num1 + num2)
    elif operator == '-':#operator 값이 - 일경우 num1, num2를 뺀다
        print(num1 - num2)
    else:
        print("해당 계산기는 / ,*, +, - 범위 내에서만 계산이 가능합니다. 다시 입력해주세요") #연산자가 입력되어 있지 않을 경우 오류 메시지 출력한다.