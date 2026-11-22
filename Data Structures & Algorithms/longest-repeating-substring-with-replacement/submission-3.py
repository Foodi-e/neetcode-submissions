class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = dict()
        leng = 1
        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            window_len = right - left + 1
            if window_len - max(count.values()) <= k:
                leng = max(window_len, leng)
            else:
                count[s[left]] -= 1
                left += 1
            right += 1
        return leng