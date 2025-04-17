import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[1]) + ' | ' + colored(board[2]) + ' | ' + colored(board[3]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[4]) + ' | ' + colored(board[5]) + ' | ' + colored(board[6]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[7]) + ' | ' + colored(board[8]) + ' | ' + colored(board[9]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

def player_move(board, symbol):
    move = 0
    while move not in range(1, 10) or not board[move].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move].isdigit():
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move] = symbol

def ai_move(board, ai_symbol, player_symbol):
    for i in range(1, 10):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(1, 10):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(1, 10) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),    # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),    # Vertical
        (1, 5, 9), (3, 5, 7)                # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board[1:])  # Skip index 0

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        board = [' '] + ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # board[0] unused
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Congratulations, " + player_name + "! You have won the game!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    turn = 'Player'
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()




