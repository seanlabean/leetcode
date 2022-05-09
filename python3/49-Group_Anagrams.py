from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list) # Hashmap for CharCounts : strs
        
        for s in strs:
            count = [0]*26 # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]

grp_anagrams = Solution().groupAnagrams(strs)
print(grp_anagrams)
