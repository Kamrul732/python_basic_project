import random
while True:
    play = input("you wanna play dice?: (y/n): ").strip().lower()
    if play == 'y':
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        print(f"you rolled: {roll1} and {roll2}\n")
    elif play == 'n':
        print("Thanks for playing:")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'")



 


print("you rolled", roll1 , roll2)