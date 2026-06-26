from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        # initialize a count for each string in strings
        for s in strs:
            c_count = [0] * 26

            for c in s:
                c_count[ord(c)-ord("a")] += 1

            ans[tuple(c_count)].append(s)
    
        return list(ans.values())

    

        