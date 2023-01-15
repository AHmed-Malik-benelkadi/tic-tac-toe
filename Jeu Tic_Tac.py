
import emoji
import essaye
def print_tic_tac_toe(values): #1 er function pour afficher le jeu tic tac toe
    print("\n") #vide
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")



def print_scoreboard(score_board): # initier la fonction pour afficher le scoreboard magique !
    print("\t--------------------------------")
    print("\t          SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


# faire la fonction pour savoir si un des deux joueur il a  win
def check_win(player_pos, cur_player):
    # toutes les combis possible pour gagné
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Dans cette boucle on va check si un des deux joueur a utilisé la combinison possible pour gagné
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            return True
    #mettre la loup en false si les combinisons ne sont paaas respectées
    return False


# Dans cette fonction on va verifier si la game n'est pas une game nul = draw
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False



def single_game(cur_player):


    values = [' ' for x in range(9)]

    # dans ce dico on va stocké les postion occupée par X ou 'O'
    player_pos = {'X': [], 'O': []}

    while True:  # cette boucle while "True" permet pour continuer à demander à l'utilisateur de saisir un mouvement valide
        print_tic_tac_toe(values)

    #   ici on  gère les entrées de l'utilisateur pour les déplacements de jeu en utilisant la fonction "input()"
        try:   #  ce  bloc try-except est utilisé pour gérer les erreurs de saisie de l'utilisateur en s'assurant qu'il entre un nombre entier valide pour le mouvement
            print(" Joueur ", cur_player, " TOUR. DE [1,9] choisir une box ! : ", end="")
            move = int(input())
        except ValueError:
            print("Mauvais !!! Ressayer ")
            continue

        # on vérifie la validité de la saisie de l'utilisateur,on verifie si le mouvement est compris entre 1 et 9
        if move < 1 or move > 9:
            print("Mauvais !!! Ressayer")
            continue

        # Cette section de code vérifie si la case ciblée par l'utilisateur pour son mouvement n'est pas déjà occupée
        if values[move - 1] != ' ': #ici on  vérifie  si cette valeur est différente de ' '(espace vide) et si c'est le cas cela signifie que la case ciblée est déjà occupée
            print(" Place deja occupée ressayé avec une autre entrée s'il vous plait ")
            continue


        # on met a jour l'etat de la gride apres le tour
        values[move - 1] = cur_player

        # ensuite on met a jour l'etat le mouvement du joeur
        player_pos[cur_player].append(move) # pour ajouter la dernière position de l'utilisateur dans la liste correspondant au joueur courant.

        # on va verifier si le joeur cur a gagné, en comparant les positions de chaque joueur avec les combinaisons gagnantes possibles
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Joueur ", cur_player,emoji.emojize(" est le plus fort donc a gagné la partie ! :trophy:"))
            print("\n")
            return cur_player

        # verifier si la game est un match nul
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print(" Partie Nul ")
            print("\n")
            return 'D'

        #  dans cette condition elle nous permet d'alterner les tours de jeu entre les joueurs
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

        


if __name__ == "__main__":

    print("Joueur  1")
    player1 = input('Bienvenu ! Quel est votre nom svp : ')
    print("\n")

    print("Joeur 2")
    player2 = input("Bienvenu ! Quel est votre nom  Joueur  2 svp : ")
    print("\n")

    cur_player = player1

    player_choice = {'X': "", 'O': ""}

    options = ['X', 'O']
     # sauvgarde du scorboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)


    while True:


        print("c'est au tour de ", cur_player)
        print("Entrer  1 pour choisir 'X' \U0001F60D")
        print(emoji.emojize("Entrer 2 pour choisir  'O':thumbs_up:"))
        print(emoji.emojize("Entrer 3 pour quitter !:pile_of_poo: "))

        # ici dans le bloc try except on va verifier si l'utilisatur a bien entrée un int (entier)
        try:
            choice = int(input())
        except ValueError:
            print("Mauvais !  ,réessayer et  inserer un entier \n")
            continue


        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("score Final  §§")
            print_scoreboard(score_board)
            break

        else:
            print("Ressayé svp entre '1 et 3' \n")

        # ici on va stocké le gagnant de la partie precedente
        winner = single_game(options[choice - 1]) # ce bout de code permet d'appeller la partie et de return le gagnant

        # si c'est pour la game si elle est en draw match nul
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        #  si le joueur actuel est "player1", il devient "player2" pour la prochaine partie et vice versa.
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1
