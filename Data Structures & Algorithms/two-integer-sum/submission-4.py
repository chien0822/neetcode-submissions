class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i #以nums[i]當key，存入其value i
            #dict[i] = dict.get(nums[i],i) 用index當key又用key去找index(全都是index)
        for j in range(len(nums)):
            need = target - nums[j]
            if dict.get(need) != j and need in dict:
                c = dict.get(need)
                return  [j,c]
