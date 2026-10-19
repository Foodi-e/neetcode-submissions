class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = set(nums)

        l = len(nums)
        for i in range(l):
            second = target - nums[i]
            for j in range(i + 1, l):
                if nums[j] == second:
                    return [i, j]
        return None
                
