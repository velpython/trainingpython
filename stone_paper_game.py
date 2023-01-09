import random 
  
def play():
    user = input("what is your choice --  'r' for rock , 'p' for paper , 's' for scissors:")
    computer = random.choice([ 'r' , 'p' , 's'])
    if user == computer:
        return ' it is a tie '
    
    if is_win (user , computer):
        return 'you Won '

    return  ' you lost'

def is_win(player , oppenent):
    if (player == 'r' and oppenent == 's' ) or (player == 's' and oppenent == 'p') or (player == 'p' and oppenent == 'r'):
        return True

print(play())

