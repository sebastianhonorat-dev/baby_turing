import random

__goal = [1,2,3,
          4,5,6,
          7,8,9]

class Node:

    def __init__(self, value, prev=None):
        self.value=value
        self.prev=None

        

    def display_cube(self,puzzle:tuple):
        # print(puzzle)
        if not puzzle:
            print(puzzle)
        else:
            for i in range(3):
                start=i*3
                end=(i+1)*3
                print(puzzle[start:end])
        print()

    def randomize_face(self):
        pieces = list(self.value)
        face = ()

        while pieces:

            index=random.randint(0,len(pieces)-1)
            piece = pieces.pop(index)

            face +=(piece,)
        self.display_cube(face)
        self.value=face
        return face


    def get_moves(self,puzzle:tuple):
        puzzle=list(puzzle)
        possible_moves = []

        blank=9
        blank_index = puzzle.index(blank)

        if not puzzle:
            return
        
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

        # print(possible_moves)
        possible_nodes=[]
        for move in possible_moves:
            self.display_cube(move)
            node = Node(move)
            
            possible_nodes.append(node)
        return(possible_nodes)
    
    
    def is_goal(self, move:list):
        if move == __goal:
            return True
        else:
            return False


root=Node([1,2,3,4,5,6,7,9,8])
root.randomize_face()
# print("Start\n",root.value,"\n")
moves_list=root.get_moves(root.value)
# print(moves)
# root.set_moves(moves)
for move in moves_list:
    child = Node(move,root)


