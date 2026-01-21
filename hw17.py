#Name:
#Class: 5th Hour
#Assignment: HW17

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
import random

def replay():
    replay = int(input('1 for replay and 2 to quit'))

    if replay == 1:
        rps()
    else:
        quit()

def rps():
    #input player hand
    playerhand = int(input('1 for rock, 2 for paper, or 3 for scissors: '))
    #inout oppentent hand\
    opponenthand =random.randint(1,3)


    #draw statement

    if playerhand == opponenthand:
        print('You draw')

    #lose statement / rock - paper / paper - scissor / scissor - rock

    elif playerhand == 1 and opponenthand == 2:
        print('You lose ')

    elif playerhand == 3 and opponenthand == 2:
        print('You lose ')

    elif playerhand == 3 and opponenthand == 1:
        print('You lose ')

    #win statement rock - scissor/ scissor - paper / paper - rock

    elif playerhand == 1 and opponenthand == 3:
        print('You win ')

    elif playerhand == 3 and opponenthand == 2:
        print('You win ')

    elif playerhand == 2 and opponenthand == 1:
        print('You win ')
    replay()
rps()


#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.