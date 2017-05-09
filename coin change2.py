def change(amount,coins):
    dp = [1] + [0] * amount
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] = dp[i] + dp[i - c]
    return dp[-1]
    
coins = [1,2,5]
amount = 5
change(amount,coins)
