# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# prices = 10 20 5 25
#          b  s        max = 10
#          10 20 5 25
#          b     s     max = 10
#          10 20 5 25
#                b s   max = 20

class Solution:
    def maxProfit(self, prices):
        b_ind = 0
        res = 0
        for s_ind in range(1,len(prices)):
            if prices[s_ind] < prices[b_ind]:
                b_ind = s_ind
            res = max(res, prices[s_ind] - prices[b_ind])
        return res

# Test 1
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

# Test 2
prices = [7,6,4,2,1]
print(Solution().maxProfit(prices))
