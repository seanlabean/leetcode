#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram0(self, s, t):
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        for l in s:
            if l in countS:
                countS[l] += 1
            else:
                countS[l] = 1
        for k in t:
            if k in countT:
                countT[k] += 1
            else:
                countT[k] = 1
  
        return countS==countT
    def isAnagram1(self,s,t):
        """
        sacrifices time O(nlogn) for space O(1)
        """
        return sorted(s)==sorted(t)

# Test 1
s = "anagram"
t = "nagaram"
print(Solution().isAnagram0(s,t))
print(Solution().isAnagram1(s,t))

# Test 2
s = "rat"
t = "car"
print(Solution().isAnagram0(s,t))
print(Solution().isAnagram1(s,t))
