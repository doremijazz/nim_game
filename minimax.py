def create_children(node):
    pass

def minimax(node):
    if node.is_terminal:
        return 0
    create_children(node)
    values = []

    for children in node.childrens:
        valeur = minimax(children)
        values.append(valeur)

    return max(values)