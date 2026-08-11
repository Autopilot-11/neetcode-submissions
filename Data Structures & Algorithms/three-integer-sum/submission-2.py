class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time complexity n^2 which means we traverse the list twice
        output = []

        nums.sort()

        for i in range(len(nums)-2):

            # Check for duplicates:
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums)-1
            goal = - nums[i]
            while left < right:
                if nums[left] + nums[right] < goal:
                    left += 1 
                elif nums[left] + nums[right] > goal:
                    right -= 1
                else:
                    output.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums [right+1]:
                        right -=1
        return output

