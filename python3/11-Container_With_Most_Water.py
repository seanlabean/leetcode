# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# |
# |
# |
# |                 0
# |                 0
# |  0--------------0
# |  0              0    0
# |  0    0         0    0
# |  0    0         0    0
# |__0____0____0____0____0______________________

# Max water area is 20 units

class Solution:
    def maxArea(self, height):
        L = 0
        R = len(height)-1
        res = 0
        
        while L < R:
            res = max(res, min(height[L],height[R])*(R-L))
            if height[L] < height [R]:
                L += 1
            elif height[L] >= height[R]:
                R -= 1
        return res

# Test 1
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))

# Test 2
height = [1,1]
print(Solution().maxArea(height))
