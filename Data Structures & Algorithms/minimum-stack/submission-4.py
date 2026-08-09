class MinStack:
    # Use two stacks, one to track last pushed, one to track min element

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_element = 2 ** 31

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_element:
            self.min_element = val
        self.min_stack.append(self.min_element)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if len(self.min_stack) > 0 :
            self.min_element = self.min_stack[-1]
        else:
            self.min_element = 2 ** 31

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
        
