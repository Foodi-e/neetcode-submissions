class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        zero_id = None
        multi = 1
        l = len(nums)
        for i in range(l):

            if nums[i] == 0:
                zero_id = i
                zero_cnt += 1
                continue

            multi *= nums[i]
        
    
        if zero_cnt > 1:
            return [0]*l

        if zero_cnt == 1:
            ans = [0] * l
            ans[zero_id] = multi
            return ans
        print(zero_cnt)
        ans = []
        for i in range(l):
            ans.append((int)(multi*(nums[i]**(-1))))
        return ans


            