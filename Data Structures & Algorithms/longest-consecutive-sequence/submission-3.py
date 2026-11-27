class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # Hash set approach
        tracker = set()
        longest = 1
        for num in nums:
            tracker.add(num)
        for num in tracker:
            if num - 1 not in tracker:
                count = 1
                while num + 1 in tracker:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest

        # longest = 1
        # tracker = dict()
        # for i in range(len(nums)):
        #     if tracker.get(nums[i]-1, 0) == 0 and tracker.get(nums[i]+1, 0) == 0:
        #         tracker[nums[i]] = 1
        #     elif tracker.get(nums[i]-1, 0) != 0:
        #         count = tracker[nums[i]-1] + 1
        #         tracker[nums[i]-1] = count
        #         tracker[nums[i]] = count
        #         longest = max(longest, count)
        #     else:
        #         count = tracker[nums[i]+1] + 1
        #         tracker[nums[i]+1] = count
        #         tracker[nums[i]] = count
        #         longest = max(longest, count)
        # return longest





                



            

        