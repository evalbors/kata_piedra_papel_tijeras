import unittest
from Game import Game

class GameTest(unittest.TestCase):

    def test_if_paper_vs_rock(self):
        game = Game()
        response = game.calculate('paper', 'rock')
        self.assertEqual('paper wins', response)

    def test_if_paper_vs_spock(self):
        game = Game()
        response = game.calculate('paper', 'spock')
        self.assertEqual('paper wins', response)

    def test_if_scissors_vs_paper(self):
        game = Game()
        response = game.calculate('scissors', 'paper')
        self.assertEqual('scissors wins', response)

    def test_if_scissors_vs_lizard(self):
        game = Game()
        response = game.calculate('scissors', 'lizard')
        self.assertEqual('scissors wins', response)

    def test_if_rock_vs_scissors(self):
        game = Game()
        response = game.calculate('rock', 'scissors')
        self.assertEqual('rock wins', response)

    def test_if_rock_vs_lizard(self):
        game = Game()
        response = game.calculate('rock', 'lizard')
        self.assertEqual('rock wins', response)

    def test_if_lizard_vs_spock(self):
        game = Game()
        response = game.calculate('lizard', 'spock')
        self.assertEqual('lizard wins', response)

    def test_if_lizard_vs_paper(self):
        game = Game()
        response = game.calculate('lizard', 'paper')
        self.assertEqual('lizard wins', response)

    def test_if_spock_vs_scissors(self):
        game = Game()
        response = game.calculate('spock', 'scissors')
        self.assertEqual('spock wins', response)

    def test_if_spock_vs_rock(self):
        game = Game()
        response = game.calculate('spock', 'rock')
        self.assertEqual('spock wins', response)

    def test_if_paper_vs_paper(self):
        game = Game()
        response = game.calculate('paper', 'paper')
        self.assertEqual('game is tied', response)

    def test_if_rock_vs_rock(self):
        game = Game()
        response = game.calculate('rock', 'rock')
        self.assertEqual('game is tied', response)

    def test_if_scissors_vs_scissors(self):
        game = Game()
        response = game.calculate('scissors', 'scissors')
        self.assertEqual('game is tied', response)

if __name__ == '__main__':
    unittest.main()
