class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        longest = 0
        for w in s:
            if w in seen:
                k = len(seen) - (seen.index(w)+1)
                if k == 0:
                    seen=[]
                else:
                    seen = seen[-k:]
            seen.append(w)
            longest=max(longest,len(seen))
        return max(longest, len(seen))