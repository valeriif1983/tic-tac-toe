def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")


def check_winner(board):
    # Перевірка рядків
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Перевірка колонок
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Отримання ходу гравця
        row = int(input(f"Гравець {current_player}, введіть рядок (0-2): "))
        col = int(input(f"Гравець {current_player}, введіть колонку (0-2): "))

        if board[row][col] != " ":
            print("Це місце вже зайняте. Спробуйте ще раз.")
            continue

        board[row][col] = current_player

        # Перевірка перемоги
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Гравець {winner} виграв!")
            break

        # Перевірка нічиєї
        if is_full(board):
            print_board(board)
            print("Нічия!")
            break

        # Зміна гравця
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
