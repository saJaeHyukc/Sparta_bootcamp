def print_arguments(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
print_arguments(
    1, # a
    2, # b
    3, 4, 5, 6, # args
    hello="world", keyword="argument" # kwargs
)

# result print
"""
1
2
(3, 4, 5, 6)
{'hello': 'hello', 'world': 'world'}
"""