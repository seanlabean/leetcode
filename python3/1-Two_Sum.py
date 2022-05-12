#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):
        hashmap = {} # num : index
        
        for ind,n in enumerate(nums):
            if (target-n) in hashmap:
                return ind, hashmap[target-n]
            else:
                hashmap[n] = ind
        return
# Test 0
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))

# Test 1
nums = [3,2,4]
target = 6
print(Solution().twoSum(nums,target))

# Test 2
nums = [3,3]
target = 6
print(Solution().twoSum(nums,target))
