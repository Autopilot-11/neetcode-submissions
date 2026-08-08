class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            key = numbers[i]
            if key not in d:
                diff = target - key
                d[diff] = i
            else:
                return [d[key]+1, i+1]

        