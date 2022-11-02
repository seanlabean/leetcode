#There is an integer array nums sorted in ascending order (with distinct values).

#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums, target):
        L = 0
        R = len(nums)-1
        while L <= R:
            M = (L+R) // 2
            if target == nums[M]:
                return M
            # mid is in Left sorted portion
            if nums[L] <= nums[M]:
                if target > nums[M] or target < nums[L]:
                    L = M+1
                else:
                    R = M-1
            # mid is in Right sorted portion
            else:
                if target < nums[M] or target > nums[R]:
                    R = M-1
                else:
                    L = M+1
        return -1
# Test 0
nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums,target))

# Test 1
nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums,target))

#Test 2
nums = [1]
target = 1
print(Solution().search(nums,target))
