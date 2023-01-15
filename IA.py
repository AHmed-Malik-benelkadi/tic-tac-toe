def ia(board, signe):
    # Vérifie si l'ia peut gagner en un coup
    i = 0
    while i < len(board):
        if board[i] == "-":
            board[i] = signe
            if check_win(board, signe):
                return i
            board[i] = "-"
        i += 1

    # Vérifie si l'adversaire peut gagner en un coup
    j = 0
    while j < len(board):
        if board[j] == "-":
            board[j] = "X" if signe == "O" else "O"
            if check_win(board, "X" if signe == "O" else "O"):
                return j
            board[j] = "-"
        j += 1

    # Choisit un emplacement au hasard parmi les disponibles
    available_spaces = [i for j in range(len(board)) if board[i] == "-"]
    return random.choice(available_spaces)


def check_win(board, signe):
    # Vérifie si un symbole a gagné sur le tableau actuel
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    i = 0
    j = 1
    k = 2
    while i < len(win_conditions):
        if board[win_conditions[i]] == board[win_conditions[j]] == board[win_conditions[k]] == signe:
            return True
        i += 1
        j += 1
        k += 1
    return False



