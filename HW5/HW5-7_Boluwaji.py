import random

ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
    
    selections()
    print

def selections():
    human_play = input('Enter selection: ')
    comp_play = random.randint(1,3)
    print(human_play)
    print(comp_play)
    if human_play == 'Rock' or 'rock' and comp_play == 3:
        print('rock wins')
    elif human_play == 'Scissors' or 'scissors' and comp_play == 2:
        print('scissors wins')
    elif human_play == 'Paper' or 'paper' and comp_play == 1:
        print('paper wins')
    elif human_play == comp_play:
        print('same play')
    elif human_play != 'Scissors' or 'scissors' or 'Rock' or 'rock' or 'Paper' or 'paper':
        print('bad input')
    else:
        print('try again')
main()
