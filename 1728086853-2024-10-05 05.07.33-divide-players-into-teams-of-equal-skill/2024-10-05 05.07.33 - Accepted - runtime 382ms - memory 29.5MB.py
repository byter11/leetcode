class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        i, j = 0, n - 1

        target = skill[j] + skill[i]
        chemistry = skill[j] * skill[i]
        j -= 1
        i += 1
        while i < j :
            if skill[j] + skill[i] != target:
                return -1
            chemistry += skill[j] * skill[i]
            j -= 1
            i += 1
        
        return chemistry