class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = max(prices)
        cur_prof = 0
        max_prof = 0
        
        for i in range(len(prices)):
            cur_prof = prices[i] - left_min
            max_prof = max(max_prof,cur_prof)
            if prices[i] < left_min:
                left_min = prices[i]

        return max_prof

        