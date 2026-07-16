# Player = {nom : str, tour : bool}
from game import play_game, input_game

def move(matches, coup):
    """
    Met à jour le nombre d'allumettes restantes.

    : parameter
        matches : nombre d'allumettes restantes
        coup : nombre d'allumettes retirées

    : type
        matches : int
        coup : int

    : return
        matches : nombre d'allumettes restantes après le coup
    """
    return matches-int(coup)

def nim_game(player1,player2):
    """
    Déroule une partie complète de Nim.

    : parameter
        player1 : premier joueur
        player2 : second joueur ou ordinateur
        node : état actuel du jeu

    : type
        player1 : Player
        player2 : Player
        node : Node

    : return
        player1 : premier joueur
        player2 : second joueur
    """
    matches = 21
    while matches > 0:
        coup, player1, player2 = input_game(player1, player2, matches)
        matches = move(matches, coup)
        print(f"Il reste {matches} allumettes")

    return player1, player2

def main (config):
    """
    Lance le programme principal.

    : parameter
        config : mode de jeu choisi

    : type
        config : str

    : return
        Aucun.
    """

    if config == "2":
        player1, player2 = play_game()
    else:
        player1 = {
            "nom": input("Nom du joueur ? "),
            "tour": True
        }
        player2 = {
            "nom": "computer",
            "tour": True
        }

    player1, player2 = nim_game(player1, player2)
    if player2["tour"]:
        print(f"{player1["nom"]} à perdu et {player2["nom"]} à gagner")
    else:
        print(f"{player2["nom"]} à perdu et {player1["nom"]} à gagner")

if __name__ == "__main__":
    config = input("2 or computer ?")
    main(config)