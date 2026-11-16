class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        freq = sorted(list(count.values()), reverse= True)
        top = [key for key, value in count.items() if value >= freq[k-1]]
        return top