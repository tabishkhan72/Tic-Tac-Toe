def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Columns
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):  # Diagonals
        return True
    return False

def is_full(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    current_player = "X"
    print("🎮 Let's play Tic-Tac-Toe!")
    print_board(board)

    while True:
        move = input(f"Player {current_player}, choose your move (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("⚠️ Invalid input. Please choose a number between 1 and 9.")
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("⚠️ That spot is already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_full(board):
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
