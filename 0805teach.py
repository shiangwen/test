
import random
ans=random.randint(1,100)
guess=0
while guess!=ans:
    guess=int(input("number:"))
    if guess > ans:
        print("too big")
    elif guess < ans:
        print("too small")
print("right!")