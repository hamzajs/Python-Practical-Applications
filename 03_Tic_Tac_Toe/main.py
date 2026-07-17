# ==================== DISPLAY FUNCTION ====================
# Function to display the current board state in a formatted 3x3 grid
def printBoard(board):
    print(f"""
    {board[1]} | {board[2]} | {board[3]}
   ---+---+---
    {board[4]} | {board[5]} | {board[6]}
   ---+---+---
    {board[7]} | {board[8]} | {board[9]}
    """)

# ==================== MAIN GAME FUNCTION ====================
# Main function that controls the overall game flow
def main():
    # ==================== GAME SETUP ====================
    # Welcome message and collect player names (only once at the start)
    print("🎮 Welcome To Tic-Tac-Toe Game 🎮")
    print("Note: Player X will play first!")
    player_name_X = input("Enter Player X's name: ")
    player_name_O = input("Enter Player O's name: ")

    # ==================== GAME LOOP (Multiple Games) ====================
    # Outer loop allows players to play multiple games
    while True:
        # ==================== REINITIALIZE FOR NEW GAME ====================
        # Reset the game board with 9 empty squares for each new game
        the_board = {
            1:" ", 2:" ", 3:" ",
            4:" ", 5:" ", 6:" ",
            7:" ", 8:" ", 9:" ",
            }

        # ==================== GAME VARIABLES ====================
        # Initialize/reset game variables for each new game
        count = 0  # Track total moves played (max 9)
        is_x_turn = True  # Control whose turn it is (X goes first)
        is_o_turn = False

        # ==================== SINGLE GAME LOOP ====================
        # Inner loop runs until someone wins or the board is full (tie)
        while True:
            
            # STEP 1: Handle Player X's turn - Get input and place X on board
            if is_x_turn:
                printBoard(the_board)
                try:
                    square = int(input("Choose a square for X (1-9): ").strip())
                except ValueError:
                    print(f"\n{'='*20}\nPlease enter numbers only (1-9)!\n{'='*20}\n")
                    continue

                if square < 1 or square > 9:
                    print("Invalid square! Please choose a number between 1 and 9.")
                    continue

                if the_board[square] == ' ':
                    the_board[square] = "X"
                    count += 1
                else:
                    print("This square is already taken! Try again.")
                    continue
            # STEP 2: Handle Player O's turn - Get input and place O on board
            else:
                printBoard(the_board)
                try :
                    square = int(input("Choose a square for O (1-9):").strip())
                except ValueError:
                    print(f"\n{'='*20}\nPlease enter numbers only (1-9)!\n{'='*20}\n")
                    continue

                if square < 1 or square > 9:
                    print("Invalid square! Please choose a number between 1 and 9.")
                    continue

                if the_board[square] == ' ':
                    the_board[square] = "O"
                    count += 1
                else:
                    print("This square is already taken! Try again.")
                    continue

            # ==================== CHECK WIN CONDITIONS ====================
            # STEP 3: Check all possible winning combinations (rows, columns, diagonals)
            # Check horizontal wins (three in a row)
            if the_board[1] == the_board[2] == the_board[3] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            elif the_board[4] == the_board[5] == the_board[6] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            elif the_board[7] == the_board[8] == the_board[9] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            # Check vertical wins (three in a column)
            elif the_board[1] == the_board[4] == the_board[7] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            elif the_board[2] == the_board[5] == the_board[8] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            elif the_board[3] == the_board[6] == the_board[9] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            # Check diagonal wins (three in diagonal)
            elif the_board[1] == the_board[5] == the_board[9] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            elif the_board[3] == the_board[5] == the_board[7] != " ":
                print(f"{player_name_X if is_x_turn else player_name_O} Won!")
                printBoard(the_board)
                break
            # Check for tie (all 9 squares filled with no winner)
            elif count == 9:
                print("It's a tie!")
                break
            else:
                print(f"{'='*20}\nYour turn now: {player_name_X if not is_x_turn else player_name_O}")
            
            # ==================== TURN MANAGEMENT ====================
            # STEP 4: Switch turns between players
            if is_x_turn:
                is_o_turn = True
                is_x_turn = False
            else:
                is_x_turn = True
                is_o_turn = False
        
        # ==================== PLAY AGAIN PROMPT ====================
        # Ask players if they want to play another game
        print("="*20)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()

        if play_again == 'n':
            print(f"Thank you for playing {player_name_X} and {player_name_O}")
            break
        elif play_again == 'y':
            print("\nstarting a new game..\n")
        else:
            print("Invalid input!")
            break

# ==================== ENTRY POINT ====================
# Execute the main function when the script runs directly          
if __name__ == "__main__":
    main()