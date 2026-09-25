class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Length check
        if len(s1) > len(s2):
            return False
        
        dict1 = {}
        dict2 = {}

        for s in s1:
            dict1[s] = dict1.get(s,0) + 1
        
        l = 0
        r = len(s1) - 1
        for s in s2[l:len(s1)]:
            dict2[s] = dict2.get(s,0) + 1

        while r+1 < len(s2):
            print(s2[l:r+1])
            print(dict2.items())
            if dict1 == dict2:
                return True
            dict2[s2[l]] -= 1
            if dict2[s2[l]] == 0:
                dict2.pop(s2[l])
            dict2[s2[r+1]] = dict2.get(s2[r+1],0) + 1
            l += 1
            r += 1
        
        if dict2 == dict1:
            return True

        return False



        