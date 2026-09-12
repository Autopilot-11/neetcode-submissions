class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        maps = {}
        for num in nums:
            if maps.get(num, "a") != "a":
                return num
            maps[num] = 1
        
        return None
