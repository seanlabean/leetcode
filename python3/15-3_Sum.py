#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

# [ -3 -3 0 1 2 3 ]       
#    a  ^       ^       _sum = a + nums[L] + nums[R]
#       L       R       increment/decrement L or R if sum is too small/too big

# [ -3 -3 0 1 2 3 ]   
#    a    ^     ^       _sum == 0
#         L     R       save [a,nums[L],nums[R]]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # dont want to consider
                continue
            
            l = i+1
            r = len(nums) - 1
            while l < r:
                _sum = a + nums[l] + nums[r]
                if (_sum > 0):
                    r -= 1
                elif (_sum < 0):
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

# Test 1
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

# Test 2
nums = []
print(Solution().threeSum(nums))

# Test 3
nums = [0]
print(Solution().threeSum(nums))
