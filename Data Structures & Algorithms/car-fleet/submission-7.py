import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position of each car = initial location + speed * time
        # Idea: zip them together, sort by first array for position, separate them

        # Safety check
        if len(position) != len(speed):
            raise ValueError("position and speed number not matching")

        # Zip and sort by position
        pairs = sorted(zip(position, speed))
        sorted_p = [pair[0] for pair in pairs]
        sorted_s = [pair[1] for pair in pairs]

        sorted_p.reverse()
        sorted_s.reverse()

        time_stack = []
        pos_stack = []
        for i in range(len(sorted_p)):
            dist = target - sorted_p[i] 
            time_needed = dist / sorted_s[i]
            if len(time_stack) == 0 or time_needed > time_stack[-1]:
                time_stack.append(time_needed)
                pos_stack.append(sorted_p[i])

        return(len(time_stack))



        