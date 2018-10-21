from random import randint, choice
from calc import eval


x = randint(0, 10)

y = randint(1, 10)

error = randint(-1, 1)

op = choice(["+", "-", "*", "/"])

r = eval(x, y, op) + error
output = "{0} {3} {1} = {2}".format(x,y,r,op)
print(output)

user_answer = input("T/F? ").upper()

if user_answer == "T":
    if r == eval(x, y, op):
        print("Correct")
    else:
        print("Wrong")
if user_answer == "F":
    if r == eval(x, y, op):
        print("Wrong")
    else:
        print("Correct")