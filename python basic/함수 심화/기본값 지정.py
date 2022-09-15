# 함수를 선언할 때 인자에 기본값을 지정해줄 수 있습니다.
EXPRESSION = {
        0: lambda x, y: x + y ,
        1: lambda x, y: x - y ,
        2: lambda x, y: x * y ,
        3: lambda x, y: x / y
    }

def calc(num1, num2, option=None): # 인자로 option이 들어오지 않는 경우 기본값 할당
    """
    option
     - 0: 더하기
     - 1: 빼기
     - 2: 곱하기
     - 3: 나누기
    """
    return EXPRESSION[option](num1, num2) if option in EXPRESSION.keys() else False

print(calc(10, 20))    # False
print(calc(10, 20, 0)) # 30
print(calc(10, 20, 1)) # -10
print(calc(10, 20, 2)) # 200
print(calc(10, 20, 3)) # 0.5