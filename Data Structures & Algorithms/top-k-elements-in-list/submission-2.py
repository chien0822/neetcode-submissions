class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        pairs = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in pairs[:k]]