class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        s = set(nums)
        seq = 0
        
        for n in s:
            cnt = 1
            if n - 1 not in s:
                while n + cnt in s:
                    cnt += 1
                seq = max(seq, cnt)
        return seq


