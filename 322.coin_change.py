def coinChange(coins, amount):
       
    rs = [0] + [amount+1]*amount
    rs[0] = 0
    for i in xrange(1, amount+1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i-c] + 1)
                # restore every value i and compare it. i-c is that there is a coin c so plus 1
                # add the previous value of i-c
                # capacity is O(amount+1)
                # time capacity is O(amount*len(coins))

    if rs[amount] == amount+1:
        #if value doesn't change, there is no changes
        return -1
    return rs[amount]
    
coins = [5]
amount = 4
coinChange(coins, amount)




def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
    mem, stk, level = {amount},{amount},0
        
    while stk:
        if 0 in mem:
            return level
        stk = {i-j for i in stk for j in coins if i>=j and i-j not in mem}
        mem.update(stk)
        level +=1
    return -1


