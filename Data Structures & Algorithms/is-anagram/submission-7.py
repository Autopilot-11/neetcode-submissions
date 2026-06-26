class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f = {}
        for c in s:
            f[c] = f.get(c,0) + 1
        for c in t:
            f[c] = f.get(c,0) - 1

        for c in f.values():
            if c != 0:
                return False

        return True
