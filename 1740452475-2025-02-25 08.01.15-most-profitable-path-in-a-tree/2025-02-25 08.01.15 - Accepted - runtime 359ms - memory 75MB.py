class Node:
    def __init__(self):
        self.children = []
        self.open_ts = float('inf')

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = defaultdict(Node)
        for u, v in edges:
            g[u].children.append(v)
            g[v].children.append(u)
        
        def bob_run(node, t, p = None):
            if node == 0:
                return True

            has_any_path = False
            for c in g[node].children:
                if c != p:
                    has_path = bob_run(c, t + 1, node)
                    if has_path:
                        g[node].open_ts = t

                    has_any_path = has_any_path or has_path
                
            return has_any_path
        
        def alice_run(node, t, p = None):
            cost = amount[node]
            if g[node].open_ts == t:
                cost //= 2
            if g[node].open_ts < t:
                cost = 0

            # print(node, cost, t)
            new_cost = -float('inf')
            if len(g[node].children) == 1 and g[node].children[0] == p:
                return cost
            
            for c in g[node].children:
                if c != p:
                    new_cost = max(new_cost, cost + alice_run(c, t + 1, node))
            
            # print(node, cost, new_cost, t)
            return new_cost
        
        bob_run(bob, 0)
        return alice_run(0, 0)

# 0 -- 4
# | 
# 2
# |
# 1 -- 3

# 2    1    0
# 0 -- 2 -- 4
# |
# | -- 5 -- 1
#           |
#           3