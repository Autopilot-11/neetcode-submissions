class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Multi-define
        l, r = 0, len(nums) - 1

        # Array would be split into two sorted arrays

        while l < r:
            mid = (r+l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]