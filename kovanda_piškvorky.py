def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))
def tic_tac_toe():
    print("Vítej ve hře Tic Tac Toe\n")
    print("=" * 40)
    print("Pravidla hry: ")
    print("Každý hráč může umístit křížek nebo kolečko za kolo na mřížku 3x3.")
    print("Vítězem se stává ten hráč, který umístí svou značku do:")
    print("* horizontální, ")
    print("* vertikální nebo ")
    print("* diagonální řady.")
    print("=" * 40)
    print("HRA ZAČÍNÁ!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["o", "x"]
    current_player = 0
    print_board(board)
    while True:
        try:
            move = int(input(f"Hráč {players[current_player]} | Zadej číslo svého tahu (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Neplatný vstup. Prosím zadej číslo mezi 1 až 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Neplatný tah. Pole je obsazené, zkuz to znovu.")
                continue
            board[row][col] = players[current_player]
            print_board(board)
            if check_winner(board, players[current_player]):
                print(f"Gratulujeme hráč {players[current_player]} je VÍTĚZ!")
                break
            if is_draw(board):
                print("REMÍZA!")
                break
            current_player = 1 - current_player
        except ValueError:
            print("Neplatný vstup. Prosím zadej číslo mezi 1 až 9.")
tic_tac_toe()
