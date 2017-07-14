def uniquePaths(m, n):
    a = [[1]*n]*m 
    for i in range(1,m):
        for j in range(1,n):
            a[i][j] = a[i][j-1] + a[i-1][j]
    return a[-1][-1]
    
    
    
print uniquePaths(3, 7)
