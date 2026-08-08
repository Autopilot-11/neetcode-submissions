class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            key = numbers[i]
            if key not in d:
                diff = target - key
                d[diff] = i
            else:
                index_1 = d[key]
                index_2 = i
                break

        return [index_1+1, index_2+1]
        