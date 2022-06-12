class Solution:
    def checkInclusion(self, s1, s2):
        # s1 smaller than s2 always
        # for a perm of s1 to be in s2, window within s2
        # must have same character occurances as s1.
        # default dict with list data type can take tuple of
        # 26 length list that can check the occurance frequency of each letter. 
        # can do this once for s1 then compare with windows of
        # equivalent size in s2.

        window_dict = [0]*26
        s1_dict = [0]*26

        for l in s1:
            s1_dict[ord(l)-ord('a')] += 1
        p1 = 0
        p2 = len(s1)-1
        for l in s2[:p2+1]:
            window_dict[ord(l)-ord('a')] += 1
        
        if window_dict == s1_dict:
            return True
        
        while p2 < len(s2)-1:

            window_dict[ord(s2[p1])-ord('a')] -= 1
            p2 += 1
            window_dict[ord(s2[p2])-ord('a')] += 1
            p1 += 1
            
            if window_dict == s1_dict:
                return True
        return False

s1 = 'ab'
s2 = 'eidbaoo'
print(Solution().checkInclustion(s1,s2))

s1 = 'a'
s2 = 'ab'
print(Solution().checkInclustion(s1,s2))

s1 = 'sdf'
s2 = 'abjiojsknqwdf'
print(Solution().checkInclustion(s1,s2))
