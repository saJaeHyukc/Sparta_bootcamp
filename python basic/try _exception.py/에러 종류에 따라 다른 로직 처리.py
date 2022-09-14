while True:
    number = input()

    #신텍스 에러는 문법적 오류라 예외처리가 불가능함
    try:
        number = int(number)
        print(10/number)
    except ValueError: # int로 변환하는 과정에서 에러가 발생했을 때
        print(f"{number}은(는) 숫자가 아닙니다.")

    except ZeroDivisionError: # 0으로 나누면서 에러가 발생했을 때
        print("0으로 나눌 수 없습니다")

    except Exception as e: # 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음 -> 파이썬 pep에 나와있다!)
        print(f"예상하지 못한 에러가 발생했습니다. error: {e}")
# except 문법 또한 if / elif 와 같이 연달아서 작성할 수 있습니다. 