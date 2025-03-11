class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        axis = [0, 1]
        direction = 1
        position = [0, 0]

        obs = defaultdict(dict)
        for o in obstacles: obs[o[0]][o[1]] = True

        mx = 0
        for c in commands:
            if c == -1 or c == -2: 
                if (c == -1 and axis[0]) or (c == -2 and axis[1]):
                    direction *= -1
                axis.reverse()
            else:
                for i in range(c):
                    x, y = position[0] + axis[0]*direction, position[1] + axis[1]*direction
                    if obs[x].get(y, False):
                        break
                    position = [x, y]
                    mx = max(mx, position[0]*position[0] + position[1]*position[1])
            # print(position)

        return mx


