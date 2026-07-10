from Node import Node
from game import play_game, input_game
from player import Player


def move(matches, coup):
    return matches-int(coup)

def nim_game(player1,player2, node):
    matches = 7
    while matches > 0:
        node.matches = matches
        coup = input_game(player1, player2, node)
        matches = move(matches, coup)
        print(f"Il reste {matches} allumettes")

    return player1, player2

def main (config):

    if config == "2":
        player1, player2 = play_game()
    else:
        player1 = Player(input("Joueur 1 nom ?"))
        player2 = Player("computer")
        player1.tour = True
        player2.tour = False

    player1, player2 = nim_game(player1, player2, Node(7, player1.name))
    if player2.tour:
        print(f"{player1.name} à perdu et {player2.name} à gagner")
    else:
        print(f"{player2.name} à perdu et {player1.name} à gagner")

if __name__ == "__main__":
    config = input("2 or computer ?")
    main(config)
