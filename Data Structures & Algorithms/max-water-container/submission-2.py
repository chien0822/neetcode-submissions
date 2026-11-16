class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0, len(heights)-1
        result = 0
        while l<r:
            base=r-l
            now = base*min(heights[l],heights[r])
            if heights[l]< heights[r]:
                l=l+1
            else:
                r=r-1
            result=max(result,now)

        return result


            
        