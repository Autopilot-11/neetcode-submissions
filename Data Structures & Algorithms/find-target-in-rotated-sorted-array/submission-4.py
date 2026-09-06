class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            # Which branch is sorted
            if nums[mid] < nums[r]:
                # Right half sorted
                # if target < nums[mid] and target < nums[r]:
                #     r = mid - 1
                # elif target > nums[mid] and target > nums[r]:
                #     r = mid - 1 
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
            else:
                # Left half sorted
                if target < nums[mid] and target > nums[l]:
                    r = mid - 1
                else: 
                    l = mid + 1


        return -1