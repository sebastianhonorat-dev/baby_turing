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

