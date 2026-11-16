class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        t = 1
        if 0 not in nums:
            for i in range(len(nums)):
                t = t*nums[i]
            for i in range(len(nums)):
                m = t/nums[i]
                results.append(int(m))
        else:
            c = nums.count(0)
            if c >= 2:
                for i in range(len(nums)):
                    results.append(0)
            if c == 1:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        t = t*nums[i]                        
                for i in range(len(nums)):
                    if nums[i] == 0:
                        results.append(t)
                    else:
                        results.append(0)
        return results
        