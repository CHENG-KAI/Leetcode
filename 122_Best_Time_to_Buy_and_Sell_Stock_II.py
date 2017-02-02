class Solution(object):
    def maxProfit(self,price):
        n = len(price)
        res = 0
        for i in range(1,n):
            if price[i]-price[i-1] > 0:
                res += price[i]-price[i-1]
        return res
        

#greedy Algorithm 
