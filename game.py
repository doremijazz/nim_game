from minimax import minimax
from player import Player


def play_game():
    player1 = Player(input("Joueur 1 nom ?"))
    player2 = Player(input("Joueur 2 nom ?"))
    player1.tour = True
    player2.tour = False
    return player1, player2


def input_game(joueur1, joueur2):
    if joueur1.tour:
        print(f"C'est le tour de {joueur1.name} de jouer")
        joueur1.tour = False
        joueur2.tour = True
    else:
        print(f"C'est le tour de {joueur2.name} de jouer")
        joueur2.tour = False
        joueur1.tour = True
    coup = (input("Combien d'allumettes souhaite tu enlever ?"))
    return coup


def input_ordi(joueur, computer, node):
    if joueur.tour:
        print(f"C'est le tour de {joueur.name} de jouer")
        joueur.tour = False
        computer.tour = True
        coup = input("Combien d'allumettes souhaite tu enlever ?")
    else:
        print(f"C'est le tour de {computer.name} de jouer")
        computer.tour = False
        joueur.tour = True
        coup = minimax(node)
    return coup