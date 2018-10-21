def add(x, y):
    r = x + y 
    return r              #process

# a = int(input("a = "))
# b = int(input("b = "))

# t = add(a, b)

# print(t)


def eval(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
   
# print(eval(10, 10, "*"))