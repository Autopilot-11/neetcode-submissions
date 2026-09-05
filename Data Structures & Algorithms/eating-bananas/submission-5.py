import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Edge case
        if len(piles) == h:
            return max(piles)
        
        # h is the max hour
        # binary search
        # if each pile contain x
        # For each pile: ceil(x/k)
        # Upper bound k = max(piles)

        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r)// 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                r = mid
            else:
                l = mid + 1
        return l
                
            

        

                
            

        