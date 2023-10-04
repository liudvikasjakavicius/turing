# PROGRAM INSTRUCTIONS:

# 1) This program prompts the user to input a white chess piece, which can either be a knight or a rook.
# 2) After successfully adding the white piece, the user can add from 1 to 16 black pieces.
# 3) To finish entering black pieces, the user can simply type "done". The program will then identify which black pieces the white piece can take.
# 4) When a user adds a correct piece, they will receive a confirmation message. In case of incorrect input, an error message will be displayed.

# EXAMPLES TO TEST:

# A White Knight at b5 can take a Black Pawn at a3.
# White Knight coordinates: "knight b5"
# Black Pawn coordinates: "pawn a3"

# A White Knight at g3 can take a Black Knight at e4.
# White Knight coordinates: "knight g3"
# Black Knight coordinates: "knight e4"

# ******************************** START OF CODING ********************************

# Define a function to check if a white piece can take a black piece
def can_take_white(piece, black_piece):
# Extract coordinates from the input pieces
    if len(piece) != 2 or len(black_piece) != 2:
        return False
    white_coords = piece[1]
    black_coords = black_piece[1]
# Get the type of white piece (e.g., "knight", "rook", etc.) and convert it to lowercase
    white_type = piece[0].lower()
# Get the type of black piece (e.g., "knight", "rook", etc.) and convert it to lowercase
    black_type = black_piece[0].lower()
# Define the rules for each type of white piece
    if white_type == "knight":
# Knights can jump to specific coordinates, so check if the black piece is at one of those positions
        return (
            (abs(ord(white_coords[0]) - ord(black_coords[0])) == 1 and abs(int(white_coords[1]) - int(black_coords[1])) == 2) or
            (abs(ord(white_coords[0]) - ord(black_coords[0])) == 2 and abs(int(white_coords[1]) - int(black_coords[1])) == 1)
        )
    elif white_type == "rook":
        # Rooks can take pieces in the same row or column
        return white_coords[0] == black_coords[0] or white_coords[1] == black_coords[1]
# Initialize lists to store white and black pieces
white_pieces = []
black_pieces = []
# Ask the user to input the white piece
while True:
    white_input = input("Please input a white chess piece. It MUST be either a 'knight' or a 'rook'. You can make your choice by entering the piece type along with its coordinates in the following format, e.g., 'knight a5'. What will your input be?: ").strip().split()
    if len(white_input) == 2 and white_input[0].lower() in ["knight", "rook"] and white_input[1][0] in 'abcdefgh' and white_input[1][1] in '12345678':
        white_pieces.append(white_input)
        break
    else:
        print("Invalid input format or piece type. Please try again.")
# Ask the user to input black pieces
while True:
    black_input = input("Please enter the black pieces. You should add at least 1 piece and up to 16 at most. (or type 'done' to finish): ").strip().split()
    if black_input[0] == "done":
        break
    elif len(black_input) == 2 and black_input[1][0] in 'abcdefgh' and black_input[1][1] in '12345678':
        black_pieces.append(black_input)
        print("Black piece added successfully.")
    else:
        print("Invalid input format or coordinates out of range. Please try again.")
# Check which black pieces the white piece can take
print("Black pieces that the white piece can take:")
white_can_take = False
for black_piece in black_pieces:
    if can_take_white(white_pieces[0], black_piece):
        print(f"{black_piece[0]} {black_piece[1]}")
        white_can_take = True
if not white_can_take:
    print("The white piece cannot take any black pieces.")
# END OF PROGRAM