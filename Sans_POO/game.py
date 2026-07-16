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
    player1 = {
        "nom": input("Nom du joueur ? "),
        "tour": True,
        "coup": 0
    }

    player2 = {
        "nom": input("Nom du joueur ? "),
        "tour": False,
        "coup": 0
    }
    return player1, player2


def input_game(joueur1, joueur2, matches):
    """
    Récupère le coup du joueur dont c'est le tour.

    : parameter
        joueur1 : premier joueur
        joueur2 : second joueur ou ordinateur

    : type
        joueur1 : Player
        joueur2 : Player

    : return
        coup : nombre d'allumettes à retirer
    """
    if joueur1["tour"]:
        print(f"C'est le tour de {joueur1["nom"]} de jouer")
        coup = (input("Combien d'allumettes souhaite tu enlever ?"))
        joueur1["tour"] = False
        joueur2["tour"] = True
        joueur1["coup"] = coup
    else:
        if joueur2["nom"] == "computer":
            coup, joueur1, joueur2 = input_ordi(joueur1, joueur2, matches)
        else:
            print(f"C'est le tour de {joueur2["nom"]} de jouer")
            joueur2["tour"] = False
            joueur1["tour"] = True
            coup = (input("Combien d'allumettes souhaite tu enlever ?"))
            joueur2["coup"] = coup
    return coup, joueur1, joueur2

def computer_move(last_human_move, matches):
    coup = 5 - int(last_human_move)

    if coup > matches:
        coup = matches

    return coup

def input_ordi(joueur, computer, matches):
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
    print(f"C'est le tour de {computer["nom"]} de jouer")
    computer["tour"] = False
    joueur["tour"] = True
    coup = computer_move(joueur["coup"], matches)
    computer["coup"] = coup
    return coup, joueur, computer