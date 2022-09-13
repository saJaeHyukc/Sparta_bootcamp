class Jss:
    def __init__(self):
        self.name = input("이름: ")
        self.age = input("나이: ")
    def show(self):
        print(f"나의 이름은 {self.name}, 나이는{self.age}입니다")
class Jss2(Jss): #상속할 때 불러올 class명을 적는다
    def __init__(self):
        super().__init__() #상속할 supper로 이전 __init__을 불러온다
        self.gender = input("성별: ")
    def show(self):
        print(f"나의 이름은 {self.name}, 성별은 {self.gender}자, 나이는{self.age}입니다")
a = Jss2()
a.show()
