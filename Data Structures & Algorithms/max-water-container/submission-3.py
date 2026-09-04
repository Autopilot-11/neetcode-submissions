class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        cur_max = 0
        while left < right:
            width = right - left
            l = heights[left]
            r = heights[right]
            height = min(l,r)

            cur_max = max(cur_max,width * height)
            if r > l:
                left += 1
            else:
                right -= 1
        
        return cur_max

        