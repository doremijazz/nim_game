class Node:
    def __init__(self, matches, player):
        self.matches = matches
        self.player = player
        self.childrens = []
        self.is_terminal = False