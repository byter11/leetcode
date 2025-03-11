class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        s = derived[0]
        for i in range(1, n):
            s = s ^ derived[i]

        return s == 0

# 1 1 0
# 0 1 0 0
# 1 1 0

# 1 1
# 0 1
# 1 1

# 1 0
# 1 1
# 0 0

# 1 0

# 1 0 0 0 0 1

# 0 1 1 1 0

# 1 0

# 0 1


# 0 1
# 1 1
# 

# 0 1 1
# 1 0 0
# 