import random

class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


def randomize_face():
    pieces = [1,2,3,
              4,5,6,
              7,8,9]
    face = ()

    while pieces:

        index=random.randint(0,len(pieces)-1)
        piece = pieces.pop(index)

        face +=(piece,)
    
    print(face)
    return face


def get_moves(puzzle:tuple):
    puzzle=list(puzzle)
    blank_index = puzzle.index(1)

    blank=1
    possible_moves = []
    if blank_index not in [0,3,6]:
        temp_puzzle=puzzle.copy()
        temp_puzzle[blank_index]=temp_puzzle[blank_index-1]
        temp_puzzle[blank_index-1]=blank
        possible_moves.append(temp_puzzle)


    if blank_index not in [2,5,8] :
        temp_puzzle=puzzle.copy()
        temp_puzzle[blank_index]=temp_puzzle[blank_index+1]
        temp_puzzle[blank_index+1]=blank
        possible_moves.append(temp_puzzle)

    if blank_index < 6: 
        temp_puzzle=puzzle.copy()
        temp_puzzle[blank_index]=temp_puzzle[blank_index+3]
        temp_puzzle[blank_index+3]=blank
        possible_moves.append(temp_puzzle)

    if blank_index >= 3:
        temp_puzzle=puzzle.copy()
        temp_puzzle[blank_index]=temp_puzzle[blank_index-3]
        temp_puzzle[blank_index-3]=blank
        possible_moves.append(temp_puzzle)

    print(possible_moves)


face=randomize_face()
get_moves(face)

from queue import Queue
import math

def BFS_Shortest_Path(Start, Goal):
    Q = Queue()
    visited = set()
    Q.put((Start, 0))
    visited.add(Start)
    min_steps = math.inf

    while not Q.empty():
        (board, steps) = Q.get()
        blank_pos = board.index(0)
        row = blank_pos // 3
        column = blank_pos % 3
        if board == Goal:
            return steps

        for dx, dy in [(0,1), (0,-1),(1,0),(-1,0)]:
            new_row = row + dx
            new_column = column + dy

            if new_row >= 0 and new_row <= 2 and new_column >= 0 and new_column <=2:
                swap_pos = new_row * 3 + new_column
                temp_board = list(board)
                temp_board[blank_pos] = temp_board[swap_pos]
                temp_board[swap_pos] = 0
                new_board = tuple(temp_board)

                if new_board not in visited:
                    visited.add(new_board)
                    Q.put((new_board, steps + 1))
    return -1

x = BFS_Shortest_Path((0,1,2,3,4,5,6,7,8),(1,2,0,3,4,5,6,7,8))
print(f"Answer is {x}")

