from random import randint

def print_board(board):
    row = " {} | {} | {} "
    hr = "\n-----------\n"
    print()
    print(row.format(*board[:3]) + hr + row.format(*board[3:6]) + hr + row.format(*board[6:]))
    print()

def check(board):
    # row check
    for i in range(0, 9, 3): 
        if board[i] == board[i+1] == board[i+2]:
            return board[i]
        
    # column check
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]
    
    # major diagonal check
    if board[0] == board[4] == board[8]:
        return board[0]
    
    # minor diagonal check
    if board[2] == board[4] == board[6]:
        return board[2]
    
    return None

def tic_tac_toe():
    board = [f'{n}' for n in range(1, 10)]
    
    print("tic-tac-toe")
    while any([x not in ['x', 'o'] for x in board]):
        if check(board):
            print_board(board)
            print(f"{check(board)} wins!")
            return

        print_board(board)
        while True:
            p = int(input("where do you want to place ")) - 1
            if board[p] not in ['x', 'o']:
                board[p] = 'x'
                break
            else:
                print("invalid position")

        if check(board):
            print_board(board)
            print(f"{check(board)} wins!")
            return
        
        if any([x not in ['x', 'o'] for x in board]):
            print_board(board)
            while True:
                p = randint(0, 8)
                if board[p] not in ['x', 'o']:
                    print(f"computer placed at {p+1}")
                    board[p] = 'o'
                    break
        
    else:
        print_board(board)
        print("it's a tie!")


if __name__ == '__main__':
    while True:
        tic_tac_toe()

        if not input("do you want to play again? [y]es/[n]o ").lower().startswith('n'):
            continue
        else:
            break
