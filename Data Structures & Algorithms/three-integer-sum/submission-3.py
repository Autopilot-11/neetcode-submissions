class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time complexity n^2 which means we traverse the list twice
        output = []

        nums.sort()

        #optimized check
        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return output

        for i,s in enumerate(nums):
            # Check for duplicates:
            if s > 0:
                break

            if i > 0 and s == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums)-1
            goal = - s
            while left < right:
                if nums[left] + nums[right] < goal:
                    left += 1 
                elif nums[left] + nums[right] > goal:
                    right -= 1
                else:
                    output.append([s,nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    
        return output

