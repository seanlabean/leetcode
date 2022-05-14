#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {}
        ans = []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        key_sort = sorted(hashmap, key=hashmap.get, reverse=True)
        for j in range(k):
            ans.append(key_sort[j])
        return ans

# Test 1
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums,k))

# Test 2
nums = [1]
k = 1
print(Solution().topKFrequent(nums,k))
