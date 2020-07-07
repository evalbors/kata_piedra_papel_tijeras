class Game:
    def calculate(self, player1, player2):

        paper = 'paper'
        rock = 'rock'
        scissors = 'scissors'
        lizard = 'lizard'
        spock = 'spock'

        if player1 == paper and (player2 == rock or player2 == spock):
            return 'paper wins'

        if player1 == scissors and (player2 == paper or player2 == lizard):
            return 'scissors wins'

        if player1 == rock and (player2 == scissors or player2 == lizard):
            return 'rock wins'

        if player1 == player2:
            return 'game is tied'

        if player1 == lizard and (player2 == spock or player2 == paper):
            return 'lizard wins'

        if player1 == spock and (player2 == scissors or player2 == rock):
            return 'spock wins'