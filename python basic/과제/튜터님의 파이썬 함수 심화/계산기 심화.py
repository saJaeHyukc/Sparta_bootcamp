class Calc:
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def plus(self):
            print(self.num1 + self.num2)
        
    def minus(self):

            print(self.num1 - self.num2)
        
    def mutiple(self):
            print(self.num1 * self.num2)

    def divide(self):
        try:
            print(self.num1 / self.num2)
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")
while True:
    try:
        num1, num2 = [int(x) for x in input().split(" ")]
        break
    except ValueError:
        print("숫자만 입력 가능합니다")

        
calc = Calc()
calc.set_number(num1, num2)
calc.plus()
calc.minus()
calc.mutiple()
calc.divide()