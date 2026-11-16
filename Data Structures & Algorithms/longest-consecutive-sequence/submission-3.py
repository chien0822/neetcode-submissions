class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for x in num_set:
            if x - 1 not in num_set:
                length = 1
                #可以改寫以下，length本身就表示k
                for k in range(1, len(num_set)):
                    if x+k in num_set:
                        length = length+1
                    else:
                        break
                longest = max(longest, length)
        return longest