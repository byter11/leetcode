class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        m = [[positions[i], healths[i], directions[i], i] for i in range(len(positions))]
        m.sort()
        # print(m)

        st = []
        i = 0
        while i < len(m):
            if m[i][2] == 'R':
                st.append([i,m[i][1]])
            elif st:
                r = st.pop()
                if r[1] > m[i][1]:
                    m[r[0]][1] -= 1
                    if r[1] > 0:
                        st.append([r[0],m[r[0]][1]])
                    m[i][1] = 0
                elif r[1] < m[i][1]:
                    m[i][1] -= 1
                    m[r[0]][1] = 0
                    i -= 1
                elif r[1] == m[i][1]:
                    m[i][1] = 0
                    m[r[0]][1] = 0
            i += 1
            # print(m)
        
        m.sort(key = lambda x: x[3])
        return [b for [a,b,c,d] in m if b > 0]