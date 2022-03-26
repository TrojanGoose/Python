from ast import If
import random

gameObjects = [7, 'tomatoes', 'bar', 'oranges', 'berry', 'coins', 'wild', 'toad', 'stick', 'water', 'cookie', 'pen', 'pencils', 'erasers', 'cast']
gameObjects1 = [7, 'tomatoes', 'bar', 'oranges', 'berry', 'coins', 'wild', 'toad', 'stick', 'water', 'cookie', 'pen', 'pencils', 'erasers', 'cast']
gameObjects2 = [7, 'tomatoes', 'bar', 'oranges', 'berry', 'coins', 'wild', 'toad', 'stick', 'water', 'cookie', 'pen', 'pencils', 'erasers', 'cast']


def play():
    amount = int(input('Enter the amount of money you are staking'))
    while (amount != 0):
        play = random.sample(gameObjects,1)
        play2 = random.sample(gameObjects1,1)
        play3 = random.sample(gameObjects2, 1)

        print(play, play2, play3)
        if play2 == play == play3:
            print('you have won')
        else:
            print('LOST')
    
        closeGame = input('Do you wana play again? Y/N: \n')
        if closeGame != 'Y':
            print('Goodbye')
            break
        else:
            continue

play() 

