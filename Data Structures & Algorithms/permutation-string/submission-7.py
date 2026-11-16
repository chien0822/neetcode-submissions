class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c,w={},{}
        l=0
        for i in range(len(s1)):
            c[s1[i]]=1+c.get(s1[i],0)

        for r in range(len(s2)):
            if (r-l+1)>len(s1):
                w[s2[l]]-=1
                if w[s2[l]]==0:
                    del w[s2[l]]
                l+=1
            w[s2[r]]=1+w.get(s2[r],0)
            if w==c:
                return True
        return False