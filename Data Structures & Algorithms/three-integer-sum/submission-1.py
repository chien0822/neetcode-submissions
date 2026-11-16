class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        results=[]
        for i in range(len(n)):
            if i != 0 and n[i] == n[i-1]:
                continue
            now=[]
            l,r = i+1, len(n)-1
            while l<r:
                sum = n[l]+n[r]
                if sum>-n[i]:
                    #sum要變小
                    r= r-1
                elif sum<-n[i]:
                    #sum要變大
                    l=l+1
                else:
                    results.append([n[i],n[l],n[r]])
                    l=l+1
                    r=r-1
                    while l < r and n[l] == n[l - 1]:
                        l += 1
        return results


