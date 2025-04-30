# Python Functions Default Arguments

def add(x=5, y=5):
    return x + y

print(add())  # 15

# Python Unlimited Arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum        

print(add(1,2,3,4,5,6), add(1,2,3), add(1,2,3,4,5,6,7,8,9,10))

# Python Keyword Arguments

def calculate(n, **kwargs):
    print(kwargs)
    n+= kwargs.get("add")
    n*= kwargs.get("multiply")
    return n

print(calculate(2, add=3, multiply=5))  # 25