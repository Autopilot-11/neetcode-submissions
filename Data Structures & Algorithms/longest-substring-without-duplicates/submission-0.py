class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # Sliding window
        l, r = 0, 0
        table = set()
        max_len = 1
        table.add(s[0])
        while r + 1 < len(s):
            if s[r+1] not in table:
                table.add(s[r+1])
                r += 1
                max_len = max(r-l+1, max_len)
            else:
                while s[r+1] in table:
                    table.discard(s[l])
                    l += 1
                table.add(s[r+1])
                r += 1
                max_len = max(r-l+1, max_len)
                
        return max_len

        # for i in range(len(s)):
        #     if s[i] in table:
        #         left += 1
        #         right += 1
        #     else:
        #         table.add(s[i])
        #         left += 1
        #         right += 1
        #         length += 1
        



        