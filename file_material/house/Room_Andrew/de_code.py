import random

with open("code_tablet.txt", "r") as f:
    password = f.read()

    if int(password[0]) == 4:
        print("i")
    else:
        print(random.choice('mnpqrtvyxz'))

    if int(password[1]) == 1:
        print("s")
    else:
        print(random.choice('abcdfghjkl'))
    
    f.close()