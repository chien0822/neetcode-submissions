class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=sorted(set(nums))
        result = 0
        now = 1
        if nums==[]:
            return 0
        for i in range(1,len(n)):
            if n[i-1]+1 == n[i]:
                now=now+1
            else:
                if now>result:
                    result=now
                now = 1
        if now>result:
            result=now
        return result