class Solution:
    def trap(self, height: List[int]) -> int:
        # With two pointer rewrite 
        n = len(height)
        left, right = 0, n-1
        maxl, maxr = height[left], height[right]
        total = 0

        while left < right:
            if maxl < maxr:
                total += maxl - height[left]
                left += 1
                maxl = max(maxl,height[left])
            else:
                total += maxr - height[right]
                right -= 1
                maxr = max(maxr,height[right])
        return total


