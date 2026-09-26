class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case Check
        if len(s) < len(t):
            return ""

        dict1 = {}
        dict2 = {}
        res = ""

        for i in t:
            dict1[i] = dict1.get(i, 0) + 1
        
        need = len(dict1)
        have = 0
        
        l = 0
        identifier = 0
        min_len = 10**6
        for r in range(len(s)):
            dict2[s[r]] = dict2.get(s[r],0) + 1
            if s[r] in dict1 and dict2[s[r]] == dict1[s[r]]:
                have += 1
            while have == need:
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    res = s[l:r + 1]
                dict2[s[l]] -= 1
                if s[l] in dict1 and dict2[s[l]] < dict1[s[l]]:
                    have -= 1
                l += 1

        return res



            
            



        
        

        