#Given a string s, find the length of the longest substring without repeating characters.

# [a b c a c]
#  L
#  R           set={a}       res=1
#  L R         set={a,b}     res=1
#  L   R       set={a,b,c}   res=3
#  L     R     set={a,b,c,a} remove s[L]
#    L   R     set={b,c,a}   res=3
#    L     R   set={b,c,a,c} remove s[L]
#      L   R   set={c,a,c}   remove s[L]
#        L R   set={a,c}     res=2

class Solution:
    def lengthOfLongestSubstring(self, s):
        l=0
        res=0
        h=set()
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l+=1
            h.add(s[r])
            res = max(res, r-l+1)
        return res


# Test 1
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

# Test 2
s = "bbbbbbb"
print(Solution().lengthOfLongestSubstring(s))

# Test 3
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
