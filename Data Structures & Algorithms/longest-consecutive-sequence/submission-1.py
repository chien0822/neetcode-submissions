class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=sorted(set(nums))
        results = []
        now = 1
        if nums==[]:
            now=0
        for i in range(1,len(n)):
            if n[i-1]+1 == n[i]:
                now=now+1
            else:
                results.append(now)
                now = 1
        results.append(now)
        output = sorted(results, reverse=True)
        return output[0]