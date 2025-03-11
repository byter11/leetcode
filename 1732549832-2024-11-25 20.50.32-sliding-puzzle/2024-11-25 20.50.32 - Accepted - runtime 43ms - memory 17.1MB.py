class Node:
    def __init__(self, board):
        self.board = board
    
    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def neighbors(self):
        i, j = self.find_blank()
        res = []
        for k, l in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if k >= 0 and l >= 0 and k < 2 and l < 3:
                board = [r[:] for r in self.board]
                board[i][j], board[k][l] = board[k][l], board[i][j]
                res.append(Node(board))
        return res

    def find_blank(self):
        for i in range(2):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        return -1, -1

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = Node(board)
        end = Node([[1,2,3], [4,5,0]])

        q = deque()
        q.append((start, 0))
        seen = set()
        while q:
            node, steps = q.popleft()
            seen.add(node)
            if node == end:
                return steps

            for n in node.neighbors():
                if n in seen:
                    continue

                q.append((n, steps + 1))

        return -1

# 4 1 0
# 5 2 3

# 4 0 1
# 5 2 3

# 4 2 1
# 5 0 3

# 4 2 1
# 0 5 3

# 1 4 3
# 4 2 0
