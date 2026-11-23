class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                m = min(m, nums[left])
                break
            
            mid = (left + right) // 2
            m = min(m, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return m
        