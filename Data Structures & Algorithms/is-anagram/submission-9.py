from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths don't match, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Compare the frequency of characters directly
        return Counter(s) == Counter(t)