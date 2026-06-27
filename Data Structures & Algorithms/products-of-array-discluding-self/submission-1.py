class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 1: With Division
        # total = 1
        # zero_count = 0

        # for num in nums:
        #     if num == 0:
        #         zero_count += 1
        #     else:
        #         total *= num
        
        # # If zero count >= 2
        # if zero_count >= 2:
        #     return [0 for i in range(len(nums))]

        # res = []
        # if zero_count == 1:
        #     for i in range(len(nums)):
        #         if nums[i] != 0:
        #             res.append(0)
        #         else:
        #             res.append(total)
        # else:
        #     for i in range(len(nums)):
        #         res.append(int(total/nums[i]))
        # return res

        # Solution 2: Without division

        # Utilize front and back

        front = 1
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            result[i] = front
            front *= nums[i]

        back = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= back
            back *= nums[i]

        return result

        