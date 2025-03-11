class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if len(goal) != n:
            return False

        for i in range(n):
            j = i
            ok = True
            for k in range(n):
                if s[j] != goal[k]:
                    ok = False
                    break
                j = (j+1)%n
                
            if ok:
                return True

        return False
                