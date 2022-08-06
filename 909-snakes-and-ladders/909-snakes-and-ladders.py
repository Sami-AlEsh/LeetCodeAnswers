class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def int_to_pos(cell):
            r = (cell - 1) // length
            c = (cell - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]
        
        length = len(board)
        board.reverse()
        visited = set()
        queue = [(1, 0)]
        visited = set()
        while len(queue) > 0:
            cell, moves = queue.pop(0)
            for i in range(1, 7):
                next_cell = cell + i
                r, c = int_to_pos(next_cell)
                print(next_cell, r, c)
                if board[r][c] != -1 : next_cell = board[r][c]
                if next_cell == length * length: return moves + 1
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, moves + 1))
        return -1