def add(*args):
    # args = (1, 2, 3, 4)
    result = 0
    for i in args:
        result += i
        
    return result

print(add())           # 0
print(add(1, 2, 3))    # 6
print(add(1, 2, 3, 4)) # 10