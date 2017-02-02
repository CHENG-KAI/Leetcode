class Solution(object):
    def maxProfit(self,price):
        n = len(price)
        if not price or len(price) < 2:
            return 0
        min_price = price[0]
        max_profit = 0
        
        for i in range(1,n):
            min_price = min(min_price,price[i])
            max_profit = max(max_profit,price[i]-min_price)
        return max_profit

#price = [0] // if price == None
#price =[]  //  if not price 

#time capacity is O(n)
#space capacity is O(1)

class Solution(object):
    def maxProfit(self,price):
        n = len(price)
        if not price or n == 0:
            return 0
        dp = [0] * n
        min_price = price[0]
        for i in range(1,n):
            dp[i] = max(dp[1-i],price[i] - min_price)
            min_price = min(min_price,price[i])
        return dp[-1]

#time capacity is O(n)
#space capacity is O(n)
        
