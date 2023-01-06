import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while  guess !=  random_number :
        guess = int(input(f'Guess a number between 1 and {x}: ')) 
        print(guess)
        if guess <  random_number :
            print('sorry , guess again . too low .')
        elif guess > random_number:
            print('sorry , guess again . too high. ')
    
    print(f"yay , you guess the correct number {random_number}")

def compueter_guess(x):
    low = 1 
    high = x 
    feedback = ''
    while feedback!= 'c':
        if low != high:
            guess = random.randint(low , high )
        else:
            guess = low 
        feedback = input (f' is {guess} too high (H) , too low (L) , or correct (c): ' )
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f' yay ! {guess} , correctly')

if __name__ == "__main__":
     
     test_name = compueter_guess(x = 458)
     test_name_guess = guess(x = 10)