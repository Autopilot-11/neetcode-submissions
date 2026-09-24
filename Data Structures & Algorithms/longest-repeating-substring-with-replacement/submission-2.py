class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            flips = r - l + 1 - max(seen.values())
            while flips > k:
                seen[s[l]] = seen[s[l]] - 1 
                l += 1
                flips = r - l + 1 - max(seen.values())
            max_len = max(max_len, r - l + 1)
        
        return max_len





