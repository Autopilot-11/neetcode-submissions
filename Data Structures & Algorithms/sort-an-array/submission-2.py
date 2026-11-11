class Solution:
    # Write a merge sort
    # Basic idea: 
    # Base case: len = 1, return array
    # split into left and right, each with a sortArray call
    # return merge(left, right)
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left,right)
        

    
    # Merge Sort with left and right list
    def merge(self, l, r):
        res = []
        left_index = 0
        right_index = 0
        
        while left_index < len(l) and right_index < len(r):
            if l[left_index] <= r[right_index]:
                res.append(l[left_index])
                left_index += 1
            else:
                res.append(r[right_index])
                right_index += 1
        
        while left_index < len(l):
            res.append(l[left_index])
            left_index += 1

        while right_index < len(r):
            res.append(r[right_index])
            right_index += 1
        
        return res
        

    
        