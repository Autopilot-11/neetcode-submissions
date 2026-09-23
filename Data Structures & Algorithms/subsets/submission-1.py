class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # First try
        # res = []
        # res.append([])
        # if len(nums) == 0:
        #     return res
        # for i in range(len(nums)):
        #     j = -1
        #     while i+j < len(nums):
        #         res.append(nums[i:i+j+1])
        #         j +=1
        # return res

        if nums == []:
            return [[]]
        
        subs = self.subsets(nums[1:])
        new_sub = []
        for sub in subs:
            s_copy = sub.copy()
            s_copy.append(nums[0])
            new_sub.append(s_copy)
        
        return subs+new_sub




        