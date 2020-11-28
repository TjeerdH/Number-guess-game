import random

x = random.randrange(100)


while True:
    count = 0
    guess = input("Guess a number between 0 and 100  ")
    try:
        if x != int(guess):
            if x % 2 == 0:
                print("It is an even number!")
                count += 1
                break
            else:
                print("It is an odd number!")
                count += 1
                break
        elif x == int(guess):
            print("Lucky guess! But you are correct!")
            exit()
    except ValueError:
        print("You don't know what a number is? Only submit numbers between 0 and 100!")
        count += 1
        continue

while True:
    try:
        guess = input("Try again!  ")
        if int(guess) != x:
            if x < 50:
                print("It is smaller then 50!")
                count += 1
                break
            elif x > 50:
                print("It is greater then 50!")
                count += 1
                break
        elif x == int(guess):
            print("You are correct! Not bad on second try!")
            exit()
    except ValueError:
        print("Really? What about numbers don't you understand? Only submit numbers between 0 and 100!")
        count += 1
        continue

while True:
    try:
        guess = input("Try again!  ")
        if int(guess) != x:
            if 0 < x < 25:
                print("It is between 0 and 25!")
                count += 1
                break
            elif 26 < x < 50:
                print("It is between 26 and 50!")
                count += 1
                break
            elif 51 < x < 75:
                print("It is between 51 and 75!")
                count += 1
                break
            elif 76 < x < 100:
                print("It is between 76 and 100!")
                count += 1
                break
        elif int(guess) == x:
            count += 1
            print(f"Well done in {count} tries! You are correct!")
            exit()
    except ValueError:
        print("Come on, You should know how this works by now! Only submit numbers between 0 and 100!")
        count += 1
        continue

if guess != x:
    while guess != x:
        try:
            guess = int(input("Try again!  "))
        except ValueError:
            print("Hey dumdum, Only submit numbers between 0 and 100!")
            count += 1
            continue
        if guess == x:
            count += 1
            print(f"You have guessed correctly! In {count} tries!")
            exit()
        elif guess < x:
            print("The answer is higher!")
            count += 1
            continue
        elif guess > x:
            print("The answer is lower!")
            count += 1
            continue
elif guess == x:
    count += 1
    print(f"Well done in {count} tries!")



