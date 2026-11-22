class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        new = []
        result = 720
        for i in range(len(timePoints)):
            value = timePoints[i].split(":")
            new.append(int(int(value[0]) * 60 + int(value[1])))

        new.sort()
        lowest = 720
        for i in range(len(new)-1):
            value = new[i+1] - new[i]
            lowest = min(value, lowest)

        lowest = min(lowest, 1440-(new[-1]-new[0]))
        return lowest



              


