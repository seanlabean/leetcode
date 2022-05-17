#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        if not s:
            return True
        for i in range(int(1+len(s)/2)):
            j = -1-i
            if s[i] != s[j]:
                return False
        return True

# Test 1
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

# Test 2
s = "race a car"
print(Solution().isPalindrome(s))

# Test 3
s = " "
print(Solution().isPalindrome(s))
