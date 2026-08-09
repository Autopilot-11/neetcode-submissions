class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n) time complexity --> Single traversal
        stack = []
        for token in tokens:
            if token == "+":
                num_1 = stack.pop()
                num_2 = stack.pop()
                num = num_1 + num_2
                stack.append(num)
                print(num)
                
            elif token == "-":
                num_1 = stack.pop()
                num_2 = stack.pop()
                num = num_2 - num_1
                stack.append(num)

            
            elif token == "*":
                num_1 = stack.pop()
                num_2 = stack.pop()
                num = num_1 * num_2
                stack.append(num)


            elif token == "/":
                num_1 = stack.pop()
                num_2 = stack.pop()
                num = int(num_2 / num_1)
                stack.append(num)
                
            else:
                num = int(token)
                stack.append(num)
            
        return stack.pop()