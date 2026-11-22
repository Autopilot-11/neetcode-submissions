class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table1 = dict()
        table2 = dict()
        for i in range(len(s)):
            if table1.get(s[i],0) == 0:
                table1[s[i]] = t[i]
            if table2.get(t[i],0) == 0:
                table2[t[i]] = s[i]
            if table1[s[i]] != t[i] or table2[t[i]] != s[i]:
                    return False
        return True
            
        