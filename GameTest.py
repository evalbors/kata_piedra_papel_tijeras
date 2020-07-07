import unittest
from Game import Game

class GameTest(unittest.TestCase):

    def test_if_paper_vs_rock(self):
        game = Game()
        player1 = 'paper'
        player2 = 'rock'
        response = game.calculate(player1, player2)
        self.assertEqual('paper wins rock', response)

    def test_if_paper_vs_scissors(self):
        game = Game()
        player1 = 'paper'
        player2 = 'scissors'
        response = game.calculate(player1, player2)
        self.assertEqual('scissors wins paper', response)

    def test_if_rock_vs_scissors(self):
        game = Game()
        player1 = 'rock'
        player2 = 'scissors'
        response = game.calculate(player1, player2)
        self.assertEqual('rock wins scissors', response)

    def test_if_paper_vs_paper(self):
        game = Game()
        player1 = 'paper'
        player2 = 'paper'
        response = game.calculate(player1, player2)
        self.assertEqual('game is tied', response)

    def test_if_rock_vs_rock(self):
        game = Game()
        player1 = 'rock'
        player2 = 'rock'
        response = game.calculate(player1, player2)
        self.assertEqual('game is tied', response)

    def test_if_scissors_vs_scissors(self):
        game = Game()
        player1 = 'scissors'
        player2 = 'scissors'
        response = game.calculate(player1, player2)
        self.assertEqual('game is tied', response)

if __name__ == '__main__':
    unittest.main()
