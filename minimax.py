from Node import Node


def create_children(node):
    node.childrens = []

    for coup in range(1, 4):
        if coup <= node.matches:
            reste = node.matches - coup

            if node.player == "player1":
                next_player = "computer"
            else:
                next_player = "player1"

            children = Node(reste, next_player)

            if reste == 0:
                children.is_terminal = True

            node.childrens.append(children)

def evaluate(node):
    if node.player == "player1":
        return -1
    else:
        return 1

def minimax(node):
    if node.is_terminal:
        return evaluate(node)

    create_children(node)
    values = []
    print(node.childrens)
    for child in node.childrens:
        valeur = minimax(child)
        values.append(valeur)

    if node.player == "computer":
        return max(values)
    else:
        return min(values)

def best_move(node):
    create_children(node)

    best_score = -float("inf")
    best_coup = None

    for child in node.childrens:
        score = minimax(child)

        coup = node.matches - child.matches

        if score > best_score:
            best_score = score
            best_coup = coup

    return best_coup