class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            d[i] = 0;

        for i in nums:
            d[i] += 1;
        ans = []
        s = sorted(d.values(), reverse=True)
        i = 0
        #d = 1 : 3
        #    2 : 2
        #    3 : 1
        #s = [3, 2, 1]
        while i < k:
            for key, v in d.items():
                if v == s[i]:
                    ans.append(key)
                    i += 1
                    if i > k - 1:
                        break
        return ans


            
            
            
        