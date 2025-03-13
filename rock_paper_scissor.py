import random

choices = {'r':'rock', 'p':'paper', 's':'scissor'}
while True:
        
    
        my_choices = input("Rock pepper Scissors ? (r/p/s):").lower()
        if my_choices not in choices:
             print("Invalid choice, please choose r or , p or s")
             continue
        c_choices = random.choice(list(choices.keys()))
        print("My choices: ", my_choices)
        print("Computer choose: ", c_choices)
        if my_choices == c_choices:
            print("Its tie")
        elif (
            (my_choices == 'r' and c_choices == 's') or
            (my_choices == 's' and c_choices == 'p') or
            (my_choices == 'p' and c_choices == 'r')):
            print('You win')
        else:
            print('you lose')
        
        c_continue = input("Contineu ?: (y/n)").lower()
        if c_continue == 'n':
            break


        

 
