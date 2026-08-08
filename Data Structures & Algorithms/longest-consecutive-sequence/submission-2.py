class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Key:
        # 1. Build set to remove duplicate
        # 2. Find sequence head
        # 3. Walk forward and checking in set
        # 4. Return a max sequence length
        max_len = 0
        seq = set()
        for num in nums:
            seq.add(num)

        for num in seq:
            if num - 1 not in seq:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in seq:
                    cur_num += 1
                    cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len

        return max_len

