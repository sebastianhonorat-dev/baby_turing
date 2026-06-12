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


def Dijkstra(Start, Goal):
    Q = []
    visited = dict()

    def pull_from_heap(Q):
        minimum=Q[0]

        last_index = len(Q)-1
        Q[0]=Q[last_index]
        Q.pop()

        current_index=0

        if len(Q) > 2:
            
            while 2 * current_index + 1 < len(Q):
                left_index = 2 * current_index + 1
                left = Q[left_index]

                if steps > left[1]:
                    temp = Q[current_index]
                    Q[current_index] = Q[left_index]
                    Q[left_index] = temp
                    current_index = left_index
    
        return minimum


    def push_to_heap(board, steps):
        Q.append((board, steps))
        current_index=len(Q)-1

        while True:
            parent_index = (current_index - 1) // 2
            parent = Q[parent_index]

            if steps < parent[1]:
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
                steps += 1

                if new_board not in visited:
                    visited[new_board]=steps
                    push_to_heap(new_board, steps)

                if visited[new_board] > steps:
                    visited[new_board]=steps
    return -1

x = Dijkstra((0,1,2,3,4,5,6,7,8),(1,2,0,3,4,5,6,7,8))
print(f"Answer is {x}")