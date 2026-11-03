class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hash_set = set()
        res = 0
        l = 0
        r = 1
        hash_set.add(s[l])
        while r < len(s):
            if s[r] in hash_set:
                res = max(res, len(hash_set))
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1

            hash_set.add(s[r])
            r += 1

        return max(res, len(hash_set))