class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        seq = 0
        
        for n in s:
            if (n - 1) not in s:
                cnt = 1
                while (n + cnt) in s:
                    cnt += 1
                seq = max(seq, cnt)
        return seq


