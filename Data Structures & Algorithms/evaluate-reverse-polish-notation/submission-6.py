class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n) time complexity --> Single traversal
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())

                
            elif token == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)

            
            elif token == "*":
                stack.append(stack.pop()*stack.pop())


            elif token == "/":
                a,b = stack.pop(), stack.pop()
                num = int(b / a)
                stack.append(num)

            else:
                num = int(token)
                stack.append(num)
            
        return stack.pop()