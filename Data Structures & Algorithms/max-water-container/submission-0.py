class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        vol = 0
        while left < right:
            cur_vol = min(heights[left], heights[right]) * (right - left)
            if(cur_vol > vol):
                vol = cur_vol
            if(heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        return vol