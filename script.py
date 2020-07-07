from Game import Game
import random

options = ['paper', 'rock', 'scissors', 'lizard', 'spock']

print('Paper, rock, scissors, lizard or spock? PLAY')

game = Game()
player1 = input()
player2 = random.choice(options)
print(player2)
print('----------------------------------------------------------')
print(game.calculate(player1, player2))
print('----------------------------------------------------------')

