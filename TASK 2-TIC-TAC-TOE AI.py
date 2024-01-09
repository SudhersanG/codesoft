import math
import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {
        'X': 1,
        'O': -1,
        'tie': 0
    }

    winner = 'X' if check_winner(board, 'X') else ('O' if check_winner(board, 'O') else None)

    if winner is not None:
        return scores[winner]

    empty_cells = get_empty_cells(board)

    if is_maximizing:
        best_score = -math.inf
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            score = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            score = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_move = None
    best_score = -math.inf
    empty_cells = get_empty_cells(board)
    for cell in empty_cells:
        board[cell[0]][cell[1]] = 'X'
        score = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row, col = map(int, input("Enter row (0-2) and column (0-2) separated by space: ").split())
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            board[row][col] = current_player
        else:
            print("AI's turn...")
            row, col = get_best_move(board)
            board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif all([cell != ' ' for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
