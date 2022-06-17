class Solution:
    def minWindow(self, s, t):
        if t == "": return ""
        
        countT = {} # counts for letters in t
        window = {} # counts for needs letters in window of s
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        have, need = 0, len(countT) # start with window 0. Only need 1 of each char in t.
        res, resLength = [-1,-1], float("infinity")
        l=0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                # update result
                if (r - l +1) < resLength:
                    res = [l, r]
                    resLength = (r-l+1)
                # check for smaller satisfying window
                # pop from left pointer of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLength != float("infinity") else ""


# Test 1
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s,t))

# Test 2
s = "a"
t = "aa"
print(Solution().minWindow(s,t))
