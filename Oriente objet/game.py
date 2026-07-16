from minimax import minimax, best_move
from player import Player


def play_game():
    """
    Initialise une partie entre deux joueurs.

    : parameter
        Aucun.

    : type
        Aucun.

    : return
        player1 : premier joueur
        player2 : second joueur
    """
    player1 = Player(input("Joueur 1 nom ?"))
    player2 = Player(input("Joueur 2 nom ?"))
    player1.tour = True
    player2.tour = False
    return player1, player2


def input_game(joueur1, joueur2, node):
    """
    Récupère le coup du joueur dont c'est le tour.

    : parameter
        joueur1 : premier joueur
        joueur2 : second joueur ou ordinateur
        node : noeud actuel du jeu

    : type
        joueur1 : Player
        joueur2 : Player
        node : Node

    : return
        coup : nombre d'allumettes à retirer
    """
    if joueur1.tour:
        print(f"C'est le tour de {joueur1.name} de jouer")
        coup = (input("Combien d'allumettes souhaite tu enlever ?"))
        joueur1.tour = False
        joueur2.tour = True
    else:
        if joueur2.name == "computer":
            coup = input_ordi(joueur1, joueur2, node)
        else:
            print(f"C'est le tour de {joueur2.name} de jouer")
            joueur2.tour = False
            joueur1.tour = True
            coup = (input("Combien d'allumettes souhaite tu enlever ?"))
    return coup


def input_ordi(joueur, computer, node):
    """
    Détermine le coup joué par l'ordinateur.

    : parameter
        joueur : joueur humain
        computer : joueur contrôlé par l'ordinateur
        node : noeud actuel du jeu

    : type
        joueur : Player
        computer : Player
        node : Node

    : return
        coup : meilleur coup calculé par Minimax
    """
    print(f"C'est le tour de {computer.name} de jouer")
    computer.tour = False
    joueur.tour = True
    coup = best_move(node)
    return coup