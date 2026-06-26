class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        flip = {}
        ans = []

        # Get the
        for num in nums:
            h[num] = h.get(num,0) + 1

        # Get the 
        l = sorted(h.items(), key = lambda item: item[1], reverse = True)
        
        for i in range(k):
            ans.append(l[i][0])

        return ans

            