#tip) set은 순서는 어느정도 정해지지만 순서가 안될 때 순서가 list로 감싸서 순서를 설정한다.
from xml.sax.handler import DTDHandler


members = [
    "lee",
    "kim",
    "park"
]

ages = [
    30,
    20,
    16
]

phone = [
    "010",
    "011",
    "018"
]
for i, member in enumerate(members): # members에 있는 요소를 실행할 수 있다
    print(f"{member}의 나이는 {ages[i]}살 이며 휴대폰 번호는 {phone[-i-1]}입니다")#phone[-i-1]으로 하면 역순으로 돌릴 수 있다
# enumerate의 정확한 뜻 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가진다
# 열거하다라는 뜻이다
# 이 함수는 순서가 있는 자료형(list, set,tuple,dictionary,string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다
