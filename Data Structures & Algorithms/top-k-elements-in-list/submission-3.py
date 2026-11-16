class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        results = heapq.nlargest(k, count.items(), key = lambda x:x[1])
        return [key for key, value in results]
        #對 results 裡的每一組 (key, value)，把 key 收集起來。

