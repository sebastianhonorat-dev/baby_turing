from queue import Queue
import math
import time
from random import randint

def randommizer(board:tuple):
    blank_pos = board.index(0)
    row = blank_pos // 3
    column = blank_pos % 3

    move_list={0:(0,1), 1:(0,-1),2:(1,0),3:(-1,0)}

    moves=randint(100,1000)

    for _ in range(moves):
        move_code = randint(0,3)
        dx,dy=move_list[move_code]
        new_row = row + dx
        new_column = column + dy

        if new_row >= 0 and new_row <= 2 and new_column >= 0 and new_column <=2:
            swap_pos = new_row * 3 + new_column
            temp_board = list(board)
            temp_board[blank_pos] = temp_board[swap_pos]
            temp_board[swap_pos] = 0
            board = tuple(temp_board)

            blank_pos = board.index(0)
            row = new_row
            column = new_column

    return board


def BFS_Shortest_Path(Start, Goal):
    start = time.perf_counter()

    Q = Queue()
    visited = set()
    Q.put((Start, 0))
    visited.add(Start)

    nodes_expanded=0

    min_steps = math.inf

    while not Q.empty():
        (board, steps) = Q.get()
        blank_pos = board.index(0)
        row = blank_pos // 3
        column = blank_pos % 3

        nodes_expanded+=1

        if board == Goal:
            end = time.perf_counter()                
            elapsed = end - start
            return steps,nodes_expanded,elapsed

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

    end = time.perf_counter()                
    elapsed = end - start
    return -1,nodes_expanded,elapsed

def Dijkstra(Start, Goal):
    start = time.perf_counter()

    Q = []
    visited = dict()
    nodes_expanded=0

    def pull_from_heap(Q):
        minimum = Q[0]

        last = Q.pop()

        if not Q:
            return minimum

        Q[0] = last
        current_index = 0

        while True:
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            smallest_index = current_index

            if left_index < len(Q) and Q[left_index][1] < Q[smallest_index][1]:
                smallest_index = left_index

            if right_index < len(Q) and Q[right_index][1] < Q[smallest_index][1]:
                smallest_index = right_index

            if smallest_index == current_index:
                return minimum

            Q[current_index], Q[smallest_index] = Q[smallest_index], Q[current_index]
            current_index = smallest_index

    def push_to_heap(board, steps):
        Q.append((board, steps))
        current_index=len(Q)-1

        while current_index > 0:
            parent_index = (current_index - 1) // 2
            parent = Q[parent_index]

            if Q[current_index][1] < parent[1]:
                temp = Q[current_index]
                Q[current_index] = Q[parent_index]
                Q[parent_index] = temp
                current_index = parent_index

            else:
                return None
            
    push_to_heap(Start, 0)
    visited[Start]=0

    while Q:
        (board, steps) = pull_from_heap(Q)

        if steps > visited[board]:
            continue

        blank_pos = board.index(0)
        row = blank_pos // 3
        column = blank_pos % 3
                
        nodes_expanded+=1

        if board == Goal:
            end = time.perf_counter()                
            elapsed = end - start
            return steps,nodes_expanded,elapsed

        for dx, dy in [(0,1), (0,-1),(1,0),(-1,0)]:
            new_row = row + dx
            new_column = column + dy

            if new_row >= 0 and new_row <= 2 and new_column >= 0 and new_column <=2:
                swap_pos = new_row * 3 + new_column
                temp_board = list(board)
                temp_board[blank_pos] = temp_board[swap_pos]
                temp_board[swap_pos] = 0
                new_board = tuple(temp_board)
                new_steps = steps + 1

                if new_board not in visited:
                    visited[new_board]=new_steps
                    push_to_heap(new_board, new_steps)

                elif visited[new_board] > new_steps:
                    visited[new_board]=new_steps
                    push_to_heap(new_board, new_steps)

    end = time.perf_counter()                
    elapsed = end - start
    return -1,nodes_expanded,elapsed


Start = (
    8, 1, 3,
    4, 0, 2,
    7, 6, 5
)

Goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

if __name__ == "__main__":
    #---BFS---
    x,y,z = BFS_Shortest_Path(Start,Goal)
    print("\nBFS steps:",x,"\nBFS boards viewed:",y,"\nBFS time elapsed:",z)
    #---Dijkstra---
    x,y,z = Dijkstra(Start,Goal)
    print("\nDijkstra steps:",x,"\nDijkstra boards viewed:",y,"\nDijkstra time elapsed:",z)


    #----RANDOMIZED----

    random_start=randommizer(Start)

    #---BFS---
    x,y,z = BFS_Shortest_Path(random_start,Goal)
    print("\nRandomized BFS steps:",x,"\nRandomized BFS boards viewed:",y,"\nRandomized BFS time elapsed:",z)
    #---Dijkstra---
    x,y,z = Dijkstra(random_start,Goal)
    print("\nRandomized Dijkstra steps:",x,"\nRandomized Dijkstra boards viewed:",y,"\nRandomized Dijkstra time elapsed:",z)
