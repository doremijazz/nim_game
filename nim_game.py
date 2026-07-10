from game import play_game, input_game




def move(matches, coup):
    return matches-int(coup)

def nim_game(player1,player2):
    matches = 7
    while matches > 0:
        coup = input_game(player1, player2)
        matches = move(matches, coup)
        print(f"Il reste {matches} allumettes")

    return player1, player2

def main ():
    player1, player2 = play_game()
    player1, player2 = nim_game(player1, player2)
    if player2.tour:
        print(f"{player1.name} à perdu et {player2.name} à gagner")
    else:
        print(f"{player2.name} à perdu et {player1.name} à gagner")

if __name__ == "__main__":
    main()
