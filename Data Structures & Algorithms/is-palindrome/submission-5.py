class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers
        left = 0
        right = len(s) - 1
    
        while left <= right:
            while not s[left].isalnum() and left < len(s)-1:
                left += 1
            while not s[right].isalnum() and right > 0:
                right -= 1
            if left > right:
                return True 
            if not s[left].lower() == s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True


        