class Game:

    def calculate(self, player1, player2):

        if player1 == 'paper' and (player2 == 'rock' or player2 == 'spock'):
            return 'paper wins'

        if player1 == 'scissors' and (player2 == 'paper' or player2 == 'lizard'):
            return 'scissors wins'

        if player1 == 'rock' and (player2 == 'scissors' or player2 == 'lizard'):
            return 'rock wins'

        if player1 == 'lizard' and (player2 == 'spock' or player2 == 'paper'):
            return 'lizard wins'

        if player1 == 'spock' and (player2 == 'scissors' or player2 == 'rock'):
            return 'spock wins'


        if player2 == 'paper' and (player1 == 'rock' or player1 == 'spock'):
            return 'paper wins'

        if player2 == 'scissors' and (player1 == 'paper' or player1 == 'lizard'):
            return 'scissors wins'

        if player2 == 'rock' and (player1 == 'scissors' or player1 == 'lizard'):
            return 'rock wins'

        if player2 == 'lizard' and (player1 == 'spock' or player1 == 'paper'):
            return 'lizard wins'

        if player2 == 'spock' and (player1 == 'scissors' or player1 == 'rock'):
            return 'spock wins'



        if player1 == player2:
            return 'game is tied'