def add(*args):
    result = 0
    for i in args:
        result += i
        
    return result

numbers = [1, 2, 3, 4]

print(add(*numbers)) # 10

"""아래 코드와 동일
print(add(1, 2, 3, 4))
"""