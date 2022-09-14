def 집까지_걸어가기():
    print(error)#선언되지 않은 변수를 호출했기 때문에 에러 발생
def 버스_탑승():
    집까지_걸어가기()
def 환승():
    버스_탑승()
def 지하철_탑승():
    환승()
def 퇴근하기():
    지하철_탑승()
    
퇴근하기()

# Traceback (most recent call last):
#   File "c:\Users\wogur\OneDrive\바탕 화면\코드\Sparta_bootcamp\python basic\statcktrace의 이해\stacktrace.py", line 12, in <module>
#     퇴근하기()
#   File "c:\Users\wogur\OneDrive\바탕 화면\코드\Sparta_bootcamp\python basic\statcktrace의 이해\stacktrace.py", line 10, in 퇴근하기
#     지하철_탑승()
#   File "c:\Users\wogur\OneDrive\바탕 화면\코드\Sparta_bootcamp\python basic\statcktrace의 이해\stacktrace.py", line 8, 
# in 지하철_탑승
#     환승()
#   File "c:\Users\wogur\OneDrive\바탕 화면\코드\Sparta_bootcamp\python basic\statcktrace의 이해\stacktrace.py", line 6, 
# in 환승
#     버스_탑승()
#   File "c:\Users\wogur\OneDrive\바탕 화면\코드\Sparta_bootcamp\python basic\statcktrace의 이해\stacktrace.py", line 4, 
# in 버스_탑승
#     집까지_걸어가기()
#   File "c:\Users\wogur\OneDrive\바탕 화면\코드\Sparta_bootcamp\python basic\statcktrace의 이해\stacktrace.py", line 2, 
# in 집까지_걸어가기
#     print(error)#선언되지 않은 변수를 호출했기 때문에 에러 발생
# NameError: name 'error' is not defined. Did you mean: 'OSError'?