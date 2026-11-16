class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}      # 記錄字元最後出現的 index
        l = 0          # 視窗左端
        longest = 0
        for r, c in enumerate(s):
            if c in last and last[c] >= l:
                l = last[c] + 1
            last[c] = r
            longest = max(longest, r - l + 1)
        return longest