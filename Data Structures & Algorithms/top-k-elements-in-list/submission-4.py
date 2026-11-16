class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] = 1 + count.get(nums[i],0)
        pairs = sorted(count.items(), key=lambda x:x[1], reverse=True)
        return [key for key, value in pairs[:k]]