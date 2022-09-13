class Jss:
    def __init__(self):
        self.name = input("이름: ")
        self.age = input("나이: ")
    def show(self):
        print(f"나의 이름은 {self.name}, 나이는{self.age}입니다")
class Jss2(Jss):
    def __init__(self):
        super().__init__()
        self.gender = input("성별: ")
    def show(self):
        print(f"나의 이름은 {self.name}, 성별은{self.gender}자, 나이는{self.age}입니다")
a = Jss2()
a.show()
