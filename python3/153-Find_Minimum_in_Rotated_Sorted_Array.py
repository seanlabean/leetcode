#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums):
        # Basic binary search setup
        L, R = 0, len(nums)-1
        res = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                # Either arr is shifted 360deg or we have just reached
                # min val with L pointer.
                res = min(res, nums[L])
                break
            M = (L + R) // 2
            if nums[M] <= nums[R]:
                # We are on "right" sorted side, search Left.
                R = M - 1
            else:
                # We are on "left" sorted side, search Right.
                L = M + 1
            res = min(res, nums[M])
        return res

# Test 0
nums = [3,4,5,1,2]
print("min = {}".format(Solution().findMin(nums))) 

# Test 1
nums = [4,5,6,7,0,1,2]
print("min = {}".format(Solution().findMin(nums)))

# Test 2
nums = [11,13,15,17]
print("min = {}".format(Solution().findMin(nums)))
