class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        w={}
        max_len=0
        for r in range(len(s)):
            w[s[r]]=1+w.get(s[r],0)
            replace=r-l+1 - max(w.values())
            while replace>k:
                w[s[l]]-=1
                l=l+1
                replace=r-l+1 - max(w.values())
            max_len=max(max_len,r-l+1)
        return max_len
        