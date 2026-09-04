class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        cur_max = 0
        while left < right:
            width = right - left
            height = min(heights[right],heights[left])
            cur_max = max(cur_max,width * height)
            print(width * height)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return cur_max

        