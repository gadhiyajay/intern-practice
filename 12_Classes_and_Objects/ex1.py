board = [' ' for _ in range(9)]


def display_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print(row1)
    print(row2)
    print(row3)


def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True

    return False


def check_draw():
    if ' ' in board:
        return False
    else:
        return True


def main():
    current_player = 'X'

    while True:
        display_board()

        if check_win(current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break
        else:
            move = input(f"Player {current_player}, enter your move (1-9): ")

            if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
                board[int(move) - 1] = current_player
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
            else:
                print("Invalid move. Try again.")


if __name__ == '__main__':
    main()
