class Solution:
    def trap(self, height: List[int]) -> int:
        container=0
        left_max=[height[0]]
        for i in range(1, len(height)):
            if height[i]>left_max[i-1]:
                left_max.append(height[i])
            else:
                left_max.append(left_max[i-1])

        right_max=[0]*len(height)
        Rnum=len(height)-1
        right_max[Rnum]=height[Rnum]
        for i in range(len(height)-2,0,-1):
            if height[i]>right_max[i+1]:
                right_max[i] = height[i]
            else:
                right_max[i] = right_max[i+1]
        
        for i in range(1, len(height)):
            container_height=min(left_max[i],right_max[i])
            add = container_height-height[i]
            if add>0:
                container=container+add
        return container
