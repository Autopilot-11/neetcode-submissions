from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        new_list = []
        for i in range(len(strs)):
            # If the current config doesn't exist yet
            if new_dict.get(frozenset(Counter(strs[i]).items()),0) == 0:
                new_dict[frozenset(Counter(strs[i]).items())] = [strs[i]]
            else:
                new_dict[frozenset(Counter(strs[i]).items())].append(strs[i])

        for j in new_dict.values():
            new_list.append(j)

        return new_list

        