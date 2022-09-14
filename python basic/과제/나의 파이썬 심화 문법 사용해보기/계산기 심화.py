class Calc:
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def plus(self):
        try:
            print(int(self.num1) + int(self.num2))
        except TypeError:
            print("숫자만 입력이 가능합니다. ")
        except ValueError:
            print("숫자만 입력이 가능합니다.")
        
    def minus(self):
        try:
            print(int(self.num1) - int(self.num2))
        except TypeError:
            print("숫자만 입력이 가능합니다")
        except ValueError:
            print("숫자만 입력이 가능합니다.")
        
    def mutiple(self):
        try:
            print(int(self.num1) * int(self.num2))
        except TypeError:
            print("숫자만 입력이 가능합니다.")
        except ValueError:
            print("숫자만 입력이 가능합니다.")
    
    def divide(self):
        try:
            print(int(self.num1) / int(self.num2))
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")
        except TypeError:
            print("숫자만 입력이 가능합니다. ")
        except ValueError:
            print("숫자만 입력이 가능합니다.")
        
calc = Calc()
calc.set_number("안녕", 12)
calc.plus()
calc.minus()
calc.mutiple()
calc.divide()