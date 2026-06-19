def display_board(board):
    for index in range(len(board)):
        if index in (2,5):
            print(f"\t{board[index]}")
            print("-"*50)

        elif index < 8:
            print(f"\t{board[index]}\t|",end="")

        else:
            print(f"\t{board[index]}")

def select_cell(board:list,player:str="",choice:int=-1):
    if player != "" and choice != -1:
        board[choice]=player
    
def get_available_cells(board):
    return set(x for x in board if x not in ("X","O"))

def set_board ():
    return list(range(9))

def detect_win(board):
    winning_arrangement = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
    )

    for winning_set in winning_arrangement:
        if board[winning_set[0]] == board[winning_set[1]]==board[winning_set[2]]=="X":
            return True,-1
        elif board[winning_set[0]] == board[winning_set[1]]==board[winning_set[2]]=="O":
            return True,1
        else:
            return False,0
        
    
def detect_draw(available_cells:set):
    return not available_cells
    
    
def game_over(board:list,available_cells:set):

    win,winner=detect_win(board)
    if win: 
        return win, winner
    if detect_draw(available_cells):
        return True,0

    return False,0

board = set_board()
available_cells = get_available_cells(board)
display_board(board)

turn = 0

while True:

    if not turn % 2:
        player= "X"

    else:
        player="O"

    try:
        cell_choice=int(input(f"\n(\"-99\" to reset the board)\nSelect an available {player} placements {available_cells}:")) #temporary

        if cell_choice not in available_cells and cell_choice != -99:
            display_board(board)
            continue
        
    except ValueError:
        display_board(board)
        continue

    
    if cell_choice == -99:
        print("RESETING...")
        board = set_board()
        available_cells = get_available_cells(board)
        display_board(board)

        turn=0
        continue

    
    select_cell(board,player,cell_choice)
    print(f"{player} selected {cell_choice}")
    
    available_cells = get_available_cells(board)
    display_board(board)

    turn+=1
    
    if turn >= 5:
        detected,detect_type = game_over(board,available_cells)
        if detected:
            if detect_type in (-1,1):
                print(f"Game Over! {player} Won!")
            else:
                print("Draw!")

            break

max_player ="O"
min_player ="X"

def Minimax(board, isMax):
    detected, score = game_over(board, get_available_cells(board))
    
    if detected:
        return score

    if isMax:
        best = -math.inf
        for cell in get_available_cells(board):
            select_cell(board,max_player,cell)
            score = Minimax(board, False)
            board[cell] = cell
            best = max(best, score)
        return best
    else:
        best = math.inf
        for cell in get_available_cells(board):
            select_cell(board,min_player,cell)
            score = Minimax(board, True)
            board[cell] = cell
            best = min(best, score)
        return best

def choose_best_move(board):
    best_score = -math.inf
    best_move = None
    for cell in get_available_cells(board):
        select_cell(board, max_player, cell)
        score = Minimax(board, False)
        board[cell] = cell

        if score > best_score:
            best_score = score
            best_move = cell
    return best_move


test_board = ["O","X","O",
              3,"X",5,
              6,7,8]

print(f"Best move is {choose_best_move(test_board)}")

"""
for cell in get_available_cells(test_board):
    select_cell(test_board, max_player, cell)
    score = Minimax(test_board, False)
    test_board[cell] = cell
    print(f"Max plays at cell {cell}, score is: {score}")
"""