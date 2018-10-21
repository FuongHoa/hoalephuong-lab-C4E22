from random import randint, choice
from calc import eval

def generate_quiz():
    x = randint(0, 10)
    y = randint(1, 10)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    r = eval(x, y, op) + error

    return [x, y, op, r]

quiz = generate_quiz()
x, y, op, r = quiz

print(quiz)
output = "{0} {3} {1} = {2}".format(x, y, r, op)
print(output)

user_answer = input("T/F? ").upper()

# if user_answer == "T":
#     if r == eval(x, y, op):
#         print("Correct")
#     else:
#         print("Wrong")
# if user_answer == "F":
#     if r == eval(x, y, op):
#         print("Wrong")
#     else:
#         print("Correct")

