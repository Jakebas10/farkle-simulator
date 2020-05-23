from player import Player
from game import Game
from dice import Dice

def main():
    player1 = Player('Jake')
    player2 = Player('Anna')
    player3 = Player('Ryan')

    players = [player1, player2, player3]
    score_to_win = 10000

    new_game = Game(players, score_to_win)

if __name__ == '__main__':
    main()
