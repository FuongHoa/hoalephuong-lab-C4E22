# import calc
# from calc import eval, add # import different functions

from calc import *

x = int(input("Enter x: "))
y = int(input("Enter y: "))
op = input("Operation (+ - * /): ")

# if op == "+":
#     r = x + y
# elif op == "-":
#     r = x - y
# elif op == "*":
#     r = x * y
# elif op == "/":
#     # if y == 0:
#     #     print("ZeroDivisionError")
#     # else:
#     #     r = x / y
#     #     print(r)
#     r = x / y
# else:
#     print("Invalid operations")
# print(x, op, y, "=", r)


# r = calc.eval(x, y, op)
r = eval(x, y, op)
print(x, op, y, "=", r)