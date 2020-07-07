import unittest
from Game import Game

class GameTest(unittest.TestCase):

    def test_if_paper_vs_rock(self):
        game = Game()
        player1 = 'paper'
        player2 = 'rock'
        response = game.calculate(player1, player2)
        self.assertEqual('paper wins', response)

    def test_if_paper_vs_spock(self):
        game = Game()
        player1 = 'paper'
        player2 = 'spock'
        response = game.calculate(player1, player2)
        self.assertEqual('paper wins', response)

    def test_if_scissors_vs_paper(self):
        game = Game()
        player1 = 'scissors'
        player2 = 'paper'
        response = game.calculate(player1, player2)
        self.assertEqual('scissors wins', response)

    def test_if_scissors_vs_lizard(self):
        game = Game()
        player1 = 'scissors'
        player2 = 'lizard'
        response = game.calculate(player1, player2)
        self.assertEqual('scissors wins', response)

    def test_if_rock_vs_scissors(self):
        game = Game()
        player1 = 'rock'
        player2 = 'scissors'
        response = game.calculate(player1, player2)
        self.assertEqual('rock wins', response)

    def test_if_rock_vs_lizard(self):
        game = Game()
        player1 = 'rock'
        player2 = 'lizard'
        response = game.calculate(player1, player2)
        self.assertEqual('rock wins', response)

    def test_if_lizard_vs_spock(self):
        game = Game()
        player1 = 'lizard'
        player2 = 'spock'
        response = game.calculate(player1, player2)
        self.assertEqual('lizard wins', response)

    def test_if_lizard_vs_paper(self):
        game = Game()
        player1 = 'lizard'
        player2 = 'paper'
        response = game.calculate(player1, player2)
        self.assertEqual('lizard wins', response)

    def test_if_spock_vs_scissors(self):
        game = Game()
        player1 = 'spock'
        player2 = 'scissors'
        response = game.calculate(player1, player2)
        self.assertEqual('spock wins', response)

    def test_if_spock_vs_rock(self):
        game = Game()
        player1 = 'spock'
        player2 = 'rock'
        response = game.calculate(player1, player2)
        self.assertEqual('spock wins', response)

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
