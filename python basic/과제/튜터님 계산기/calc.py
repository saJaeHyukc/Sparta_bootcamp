#튜터님이 하신 계산기
#이것을 보고 느낀점 따로 조건문을 딕셔너리로 저장 // 딕셔너리에 람다식도 넣을 수 있어???? 맞다 다 함수든 클래스든 다 넣을 수 있다!! 만능이네...
#num1, operator, num2를 연속으로 변수 사용한 것

EXPRESSION = {
    "+" : lambda x,y: x+y,
    "*" : lambda x,y: x*y,
    "-" : lambda x,y: x-y,
    "/" : lambda x,y: x/y
}

def calc(num1, operator, num2):
    return EXPRESSION[operator](int(num1), int(num2))