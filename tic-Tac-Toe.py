A=input("enter the name of first player")
B=input("enter the name of second player")


def draw_board(board):
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def is_winner(board, player):
    return (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    )

def is_board_full(board):
    return all(cell != " " for cell in board)

def get_player_move(player, board):
    position = int(input(f"{player}'s turn (1-9): ").strip())
    while board[position - 1] != " ":
        print("That position is already taken!")
        position = int(input(f"{player}'s turn (1-9): ").strip())
    return position - 1

def play_game():
    player1 = input("Enter name for player 1 (X): ")
    player2 = input("Enter name for player 2 (O): ")
    board = [" " for _ in range(9)]
    current_player = player1

    while True:
        draw_board(board)
        position = get_player_move(current_player, board)
        board[position] = "X" if current_player == player1 else "O"

        if is_winner(board, "X"):
            draw_board(board)
            print(f"{player1} wins!")
            break
        elif is_winner(board, "O"):
            draw_board(board)
            print(f"{player2} wins!")
            break
        elif is_board_full(board):
            draw_board(board)
            print("It's a tie!")
            break

        current_player = player2 if current_player == player1 else player1
play_game()

