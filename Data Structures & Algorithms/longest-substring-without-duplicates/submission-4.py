class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        longest = 0
        for w in s:
            if w not in seen:
                seen.append(w)
            else:
                longest=max(longest,len(seen))
                k = len(seen) - (seen.index(w)+1)
                if k == 0:
                    seen=[]
                else:
                    seen = seen[-k:]
                seen.append(w)
        return max(longest, len(seen))