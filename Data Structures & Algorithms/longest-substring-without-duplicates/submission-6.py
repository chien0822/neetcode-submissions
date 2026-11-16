class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        longest = 0
        for w in s:
            if w in seen:
                seen = seen[seen.index(w) + 1:]
            seen.append(w)
            longest = max(longest, len(seen))
        return longest