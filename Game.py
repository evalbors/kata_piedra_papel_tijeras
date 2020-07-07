class Game:
    def calculate(self, player1, player2):
        paper = 'paper'
        rock = 'rock'
        scissors = 'scissors'

        if player1 == paper and player2 == rock:
            return 'paper wins rock'

        if player1 == paper and player2 == scissors:
            return 'scissors wins paper'

        if player1 == rock and player2 == scissors:
            return 'rock wins scissors'

        if player1 == paper and player2 == paper or player1 == rock and player2 == rock or player1 == scissors and player2 == scissors:
            return 'game is tied'
