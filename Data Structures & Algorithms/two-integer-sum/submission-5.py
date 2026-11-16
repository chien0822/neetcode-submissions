class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # key: ____, value: ____
        for i, num in enumerate(nums): #自動存成index和key
            need = target - num
            if need in seen:
                return [seen[need],i]
            seen[num] = i