class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dict但key是tuple，value是字
        group = {}
        for i in range(len(strs)):
            count = [0]*26
            w = strs[i]
            for j in range(len(strs[i])):
                count[ord(w[j])-97] += 1
            key = tuple(count)
            if key not in group:
                group[key] = []
            group[key].append(strs[i])
        return list(group.values())