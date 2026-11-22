class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        if len(skill) == 2:
            return skill[0]*skill[1]

        skill.sort()
        left = 1
        right = len(skill) - 2
        prev = skill[0] + skill[-1]
        total = skill[0] * skill[-1]

        while left < right:
            score = skill[left] + skill[right]
            if score != prev:
                return -1
            else:
                total += skill[left]*skill[right]
                left += 1
                right -= 1

        return total


        


