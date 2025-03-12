import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        if guess == number:
            print("Congratulations! you guessed the number")
            break
        elif guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
    except ValueError:
        print("please! Enter a valid number")



   

