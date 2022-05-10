#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False

nums1 = [1,1,1,3,3,4,3,2,4,2]
soln1 = Solution().containsDuplicate(nums1)
print(nums1, ": ", soln1)

nums2 = [1,2,3,4]
soln2 = Solution().containsDuplicate(nums2)
print(nums2, ": ", soln2)
