from random import randint

x = randint(0, 10)

y = randint(1, 10)

error = randint(-1, 1)

z = x + y + error

output = "{0} + {1} = {2}".format(x,y,z)
print(output)

user_answer = input("T/F? ").upper()

if user_answer == "T":
    if error == 0:
        print("Correct")
    else:
        print("Wrong")
if user_answer == "F":
    if error == 0:
        print("Wrong")
    else:
        print("Correct")