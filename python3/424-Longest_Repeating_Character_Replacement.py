# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s, k):
        charCount = {}
        L = 0
        res = 0
        for R in range(len(s)):
            charCount[s[R]] = 1 + charCount.get(s[R], 0)
            if (R-L+1) - max(charCount.values()) > k:
                charCount[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res

# Test 1
s,k = 'ABBB',2
print(Solution().characterReplacement(s,k))

# Test 2
s,k = 'ASDKFJFUIOIWFNADJKFBASD',1
print(Solution().characterReplacement(s,k))
