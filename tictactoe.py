import random
# Step 1: Initialize the Tic-Tac-Toe board as a 3x3 grid
board = [[" " for _ in range(3)] for _ in range(3)]
# Step 2: Define a function to display the current state of the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")
# Step 3: Define a function to check if a player (X or O) has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
# Step 4: Define a function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)
# Step 5: Define a function for the computer's move (random)
def computer_move(board):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[y][x] == " ":
            return x, y
# Step 6: Define the main game loop
def play_game():
    player_turn = True  # True for the player, False for the computer
    while True:
        print_board(board)
        if player_turn:
            move = input("Enter your move (x, y): ")
            x, y = map(int, move.split(","))
            if board[y][x] == " ":
                board[y][x] = "X"
            else:
                print("Invalid move. Try again.")
                continue
        else:
            x, y = computer_move(board)
            board[y][x] = "O"
        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_winner(board, "O"):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        player_turn = not player_turn
# Step 7: Start the game when the script is run
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()