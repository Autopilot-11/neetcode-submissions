from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ')' and not top == '(':
                    return False
                if c == '}' and not top == '{':
                    return False
                if c == ']' and not top == '[':
                    return False
        return len(stack) == 0