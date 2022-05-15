#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest=0
        for n in nums:
            if (n-1) not in numSet:
                length=1
                while (n+length) in numSet:
                    length+=1
                longest = max(longest,length)
        return longest

# Test 1
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))

# Test 2
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))
