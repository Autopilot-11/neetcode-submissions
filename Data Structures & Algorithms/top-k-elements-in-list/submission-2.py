class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This question uses the bucket sort algorithm

        # Allocate buckets & initialize count
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        ans = []

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for num, f in count.items():
            freq[f].append(num)

        for i in range(len(freq)):
            for num in freq[len(freq)-i-1]:
                ans.append(num)
                if len(ans) == k:
                    return ans

            